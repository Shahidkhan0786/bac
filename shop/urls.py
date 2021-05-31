from django.contrib import admin
from django.urls import path
from . import views
from .views import Login,Signup

urlpatterns = [
path('', views.index, name="ShopHome"),
path('products/', views.product, name="ShopProduct"),
path('cproducts/', views.cproduct, name="ShopProduct"),
path('bgproducts/', views.bgproducts, name="bgProduct"),
path('bgproducts/<int:id>/',views.bgproduct_detail ,name="bgproductdetail"),
path('desc/', views.product_disc, name="p-disc"),



path('motherboard/', views.motherboard, name="mobo"),
path('ram/', views.ram, name="ram"),
path('about/', views.about, name="about"),
path('contact/', views.contact, name="contact"),
path('login/', Login.as_view(), name="login"),
path('signup/', Signup.as_view(), name="signup"),
path('cart/', views.cart, name="cart"),
path('cpup/' , views.cpu ,name="product_cpu"),
path('logout/',views.logout , name="logout" ),
path('cool/',views.cooler , name="cooler" ),
path('cases/',views.case , name="cases" ),
path('psux/',views.PSU , name="psux" ),
path('storagee/',views.Storagee , name="storagee" ),
path('graphiccard/',views.graphic_card , name="gcard" ),
path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/")),
path('profile/<int:pk>', views.MyProfileDetailView.as_view()),


    # build
path('cpu/',views.build_cpu , name="buildcpu" ),
path('buildhome/', views.build_home, name="buildhome"),
path('mobo/', views.build_mobo, name="builmobo"),
path('ramb/', views.build_ram, name="builram"),
path('graphicx/', views.build_Graphicx, name="builgraphic"),
path('storagex/', views.build_Storage, name="builstorage"),
path('smpsx/', views.build_Psu, name="builsmps"),
path('casesx/', views.build_Cases, name="builcases"),
path('delxx/', views.delx, name="deletex"),
path('savebuild/', views.save_build, name="savebuild"),


    # /////////usrdashbord
path('usrdashbord/', views.usr_dashbord, name="userdashbord"),
path('usrbuilds/', views.usr_builds, name="userbuilds"),
path('bloghomee/', views.blog_Home, name="userbloghome"),
path('createblog/', views.user_blogg, name="createblog"),
path('viewblog/'  , views.user_bloglist , name="bloglistt"),
path('delusrbuild/<int:id>/'  , views.del_userbuilds , name="delusrbuilds"),
path('delbx/<int:id>/' , views.delbl ,name="delblg"),
# path('editub/<int:id>/' ,views.edit_userbuilds , name="edituserbuilds"),

    # sepratedelete the builds
path('delxxy/' ,  views.delcpu , name="delcpuu"),
path('delxxm/' ,  views.delmobox , name="delmobo"),
path('delxxram/' ,  views.delramx , name="delram"),
path('delxxgnam/' ,  views.delgraphicx , name="delgraphic"),
path('delxxdnam/' ,  views.delstoragex , name="delstorage"),
path('delxxps/' ,  views.delpowerx , name="delpsux"),
path('delxxcase/' ,  views.delcasex , name="delcasex"),


    # vendorsignup

path('vendor-sign/' ,  views.vendor_signup , name="vendorss"),


    # cart


path('cart/<int:id>/' , views.add_to_cart , name="adddtocart"),
path('showcart/' , views.show_cart , name="showcartx"),
path('pluscart/' , views.plus_cart),
path('minuscart/' , views.minus_cart),

path('removecart/' , views.remove_cart),

path('checkout/' , views.check_out),
path('payment/' , views.payment),
path('orders/' , views.orders),


path('complete-builds-detail/<int:id>/' , views.complete_builds_detail),
path('builds-product-detail/' , views.builds_product_detail),

path('buy/<int:id>/' , views.buy_builds),

# path('buildrecipt/' , views.b),




]
