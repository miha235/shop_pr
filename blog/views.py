# blog/views.py
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import BlogPost
from django.utils.text import slugify


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "blogposts"
    success_url = reverse_lazy("blog:blogpost_list")

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "blogpost"
    success_url = reverse_lazy("blog:blogpost_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/blogpost_form.html"  # шаблон для формы создания поста
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy(
        "blog:blogpost_list"
    )  # куда перенаправлять после создания поста

    def form_valid(self, form):
        # Генерируем slug из поля
        blog_post = form.save(commit=False)
        blog_post.slug = slugify(blog_post.title)
        blog_post.save()
        return super().form_valid(form)

    # После создания статьи перенаправляем на страницу с её подробностями
    def get_success_url(self):
        return reverse_lazy("blog:blogpost_detail", kwargs={"slug": self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/blogpost_form.html"
    fields = ["title", "content", "preview_image", "slug", "is_published"]
    success_url = reverse_lazy("blog:blogpost_list")

    def form_valid(self, form):
        # Обновляем slug, если заголовок был изменен
        blog_post = form.save(commit=False)
        blog_post.slug = slugify(blog_post.title)
        blog_post.save()
        return super().form_valid(form)

    # После обновления статьи перенаправляем на страницу с её подробностями
    def get_success_url(self):
        return reverse_lazy("blog:blogpost_detail", kwargs={"slug": self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    context_object_name = "blogpost"

    # После удаления перенаправляем на страницу списка статей
    success_url = reverse_lazy("blog:blogpost_list")
