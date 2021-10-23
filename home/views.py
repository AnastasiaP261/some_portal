from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import *


class Home(ListView):
    template_name = 'home/home_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['news'] = News.objects.order_by('created_at').reverse()[:4]
        return context

    def get_queryset(self):
        return Publications.objects.order_by('created_at').reverse()


class DetailPost(DetailView, UpdateView):
    template_name = 'home/detail.html'
    model = News
    fields = ['likes_num', 'dislikes_num']
    linked_likes_table = None  # обязательно переопределить!
    linked_likescomm_table = None  # обязательно переопределить!
    linked_comm_table = None  # обязательно переопределить!
    linked_url_name = None  # обязательно переопределить!

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)

        res = self.linked_likes_table.objects.filter(id_user=self.request.user.id, id_posts=self.kwargs['pk'])
        context['button_visible'] = False if len(res) else True

        # context['comments'] = CommentNews.objects.filter(id_post=self.kwargs['pk'])
        context['comments'] = self.linked_comm_table.objects.raw(self.get_likescomment_request(
            commentpost_table=self.linked_comm_table._meta.db_table,
            likescommentpost_table=self.linked_likescomm_table._meta.db_table,
            post_id=self.kwargs['pk'],
            user_id=self.request.user.id))

        if not len(context['comments']):
            context['comments'] = 'no_comm'

        return context

    def post(self, request, *args, **kwargs):
        try:
            pk = None
            if 'like_type' and 'comm_id' in request.POST:
                pk = kwargs['pk']
                kwargs['pk'] = request.POST['comm_id']
                kwargs['addit_table'] = self.linked_likescomm_table
                self.edit_likes(self.linked_comm_table, request, *args, **kwargs)
            elif 'like_type' in request.POST:
                kwargs['addit_table'] = self.linked_likes_table
                pk = self.edit_likes(self.model, request, *args, **kwargs)
            elif 'new_comm' in request.POST:
                kwargs['comm_table'] = self.linked_comm_table
                pk = self.new_comment(self, request, *args, **kwargs)
            return redirect(self.linked_url_name, pk=pk)
        except:
            return redirect('home')

    @staticmethod
    def get_likescomment_request(commentpost_table, likescommentpost_table, post_id, user_id):
        req = f"""
            select {commentpost_table}.id, 
                {commentpost_table}.id_user_id, 
                {commentpost_table}.id_post_id, 
                likes_num, 
                dislikes_num, 
                `text`, 
                {commentpost_table}.created_at,
                likes.`like`,
                likes.id_user_id,
                likes.id_posts_id
            from {commentpost_table} 
            left join (
                SELECT `like`,
                    id_user_id,
                    id_posts_id
                from {likescommentpost_table} 
                where id_user_id == {user_id}) as likes 
            on likes.id_posts_id={commentpost_table}.id
            where {commentpost_table}.id_post_id == {post_id}
            """

        return req

    @staticmethod
    def new_comment(cls, request, *args, **kwargs):
        comm_table = kwargs['comm_table']
        usr_pk = request.user.id  # ид юзера
        comm_text = request.POST['new_comm']

        obj = comm_table.objects.create(id_user=User.objects.get(pk=usr_pk),
                                        id_post=cls.model.objects.get(pk=kwargs['pk']),
                                        text=comm_text)
        obj.save()

        return kwargs['pk']

    @staticmethod
    def edit_likes(model, request, *args, **kwargs):
        obj = model.objects.get(pk=kwargs['pk'])  # объект поста(новости/публикации/комментария)
        addit_table = kwargs['addit_table']  # соответствующая доп таблица для связи с пользователем
        usr_pk = request.user.id  # ид юзера

        # проверка, оценивал ли уже юзер этот пост
        user_likes = addit_table.objects.filter(id_user=usr_pk, id_posts=kwargs['pk'])
        if len(user_likes) == 0:
            like_type = request.POST['like_type']  # тип оценки(лайк/дизлайк)
            if like_type == 'like':
                obj.likes_num += 1
            elif like_type == 'dislike':
                obj.dislikes_num += 1
            obj.save()

            addit_table.objects.create(id_user=User.objects.get(pk=usr_pk),
                                       id_posts=obj,
                                       like=(True if like_type == 'like' else False))
        return kwargs['pk']


class DetailNew(DetailPost):
    model = News
    linked_likes_table = LikesNews
    linked_likescomm_table = LikesCommentNews
    linked_comm_table = CommentNews
    linked_url_name = 'new'


class DetailPublication(DetailPost):
    model = Publications
    linked_likes_table = LikesPublications
    linked_likescomm_table = LikesCommentPublication
    linked_comm_table = CommentPublication
    linked_url_name = 'publication'


