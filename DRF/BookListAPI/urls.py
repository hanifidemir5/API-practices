from django.urls import path,include
from . import views
urlpatterns = [
    # path('books/',views.books),
    path('books/',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),
    path('menu-items',views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>',views.SingleMenuItemView.as_view()),
    path('menu-items2',views.menu_items),
    path('menu-items2/<int:id>',views.single_item),

]