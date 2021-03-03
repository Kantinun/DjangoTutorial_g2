from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.index, name='index'), # ไปหน้าเเรก(คำศัพท์ทั้งหมด)
    path('<int:vocab_id>/', views.detail , name='detail'), # ไปหน้ารายละเอียดของคำศัพท์(แสดงคำศัพท์และความหมายทั้งหมด)
    path('addPage/', views.addWordPage , name='addPage'),   # ไปหน้าเเรก()
    path('add/', views.addWord , name='add'), # ไปหน้าเพิ่มคำศัพท์
    path('search/',views.search, name='search'),# ไปคำสั่งค้นหาข้อมูล()
    path('<int:vocab_id>/editWordPage/',views.editWordPage,name='editWordPage'),
    path('<int:vocab_id>',views.editWord,name='edit'),
    path('<int:vocab_id>/delete/', views.delete , name='delete'),
    path('<int:vocab_id>/<int:def_id>/editDefpage/',views.editDefPage,name='editDefpage'),
    path('<int:vocab_id>/<int:def_id>/editDef/',views.editDef,name='editDef')
]