from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from shop.forms import vendorx, VendorUserForm
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from .models import Product, cart
from .models import Category, Smps, Graphic_Card, Storage, Display_ports, CPU, vendor, ram as Ram, Motherboard
from .models import Customer, MyProfile, Case, Build_PC, orderplaced, builds_guides
from blog.models import post, Catagory
from django.contrib import messages

from django.http import HttpResponse, Http404
from blog.models import Contact

p = ""


def index(request):
    global p
    if (request.user.is_authenticated):
        try:
            c = MyProfile.objects.get(user=request.user)
            p = c.pic

        except:
            messages.error(request, "jii")
        user1 = request.user
        m1 = MyProfile.objects.get(user=user1)
        # equipments = [equipment.name for equipment in ]
        request.session['export'] = m1.name
        print(m1.name)
        print("===============================================")
    return render(request, 'shop/index.html', {'pic': p})


class Login(View):
    def get(self, request):
        return render(request, 'shop/login.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        error_message = None
        if (customer):
            flag = check_password(password, customer.password)
            if (flag):
                request.session['cname'] = customer.email
                request.session['c_id'] = customer.id
                # print('you are' , request.session.get('cname'))
                return redirect("ShopHome")
            else:
                error_message = "Please enter correct username or password !!"
                return render(request, 'shop/login.html', {'error': error_message})
        else:
            error_message = "Please enter correct username or password !!"
            return render(request, 'shop/login.html', {'error': error_message})


class Signup(View):
    def get(self, request):
        return render(request, 'shop/signup.html');

    def post(self, request):
        print('postttttttttt&&&&&&&&&&&&&')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passd = request.POST.get('pass')
        # validation
        value = {
            'first_name': fname,
            'last_name': lname,
            'email': email
        }
        error_message = None
        customer = Customer(f_name=fname,
                            l_name=lname,
                            email=email,
                            password=passd)

        error_message = self.validateCustomer(customer)

        if not error_message:

            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'shop/signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.f_name):
            error_message = "First Name Required !!"
        elif len(customer.f_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.l_name:
            error_message = 'Last Name Required'
        elif len(customer.l_name) < 4:
            error_message = 'Last Name must be 4 char long or more'

        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message

    # customer.password = make_password(customer.password)
    # customer.register()
    # return redirect("login")


def product(request):
    prod = Product.objects.all()
    category = Category.get_all_categories
    # category = request.GET.get('category')
    # if(category):
    #     prod = Product.get_all_products_byid(category)
    #     print(category)
    # else:
    #     prod = Product.get_all_products()

    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def logout(request):
    request.session.clear()
    return redirect("ShopHome")


def cooler(request):
    prod = Product.objects.filter(category_id=8)

    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    return render(request, 'shop/product.html', data)


def graphic_card(request):
    prod = Product.objects.filter(category__name='graphicCard')

    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    return render(request, 'shop/product.html', data)


def case(request):
    prod = Product.objects.filter(category__name='case')

    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    return render(request, 'shop/product.html', data)


def cproduct(request):
    prod = Build_PC.objects.all()

    category = Category.get_all_categories
    # category = request.GET.get('category')
    # if(category):
    #     prod = Product.get_all_products_byid(category)
    #     print(category)
    # else:
    #     prod = Product.get_all_products()

    data = {}
    data['product'] = prod
    data['category'] = category

    return render(request, 'build/comp-builds.html', data)


def complete_builds_detail(request, id):
    d = ""
    if request.method == "POST":
        idd = request.POST['iddd']
        print(idd)
        d = Build_PC.objects.get(id=idd)
        print(d)
    data = {"product": d}
    return render(request, 'build/completebuild-detail.html', data)


def builds_product_detail(request):
    return render(request, 'build/build-product-detail.html')


def bgproducts(request):
    prod = Product.objects.filter(category_id=2)

    category = Category.get_all_categories
    prod = builds_guides.objects.all()
    # category = request.GET.get('category')
    # if(category):
    #     prod = Product.get_all_products_byid(category)
    #     print(category)
    # else:
    #     prod = Product.get_all_products()

    data = {}
    data['product'] = prod
    data['category'] = category
    return render(request, 'shop/build_guide.html', data)


def bgproduct_detail(request, id):
    prod = builds_guides.objects.get(id=id)

    d = {"data": prod}
    return render(request, 'shop/build-guide-detail.html', d)


def cpu(request):
    prod = Product.objects.filter(category__name='processor')
    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def Storagee(request):
    prod = Product.objects.filter(category__name='storage')
    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def motherboard(request):
    prod = Product.objects.filter(category__name='mobo')
    category = Category.get_all_categories

    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def ram(request):
    prod = Product.objects.filter(category__name='ram')

    category = Category.get_all_categories
    print('xxxxxxxxxxxxxxxxxx')
    print(prod.query)
    print(category)
    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def PSU(request):
    prod = Product.objects.filter(category__name='powersupply')

    category = Category.get_all_categories

    print(category)
    data = {}
    data['product'] = prod
    data['category'] = category
    data['cname'] = request.session.get('cname')
    return render(request, 'shop/product.html', data)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print("=========================")
        print(name)
        print("=========================")
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            try:
                ctx = {
                    'user': "Shahid"
                }
                message = get_template('mailtemp.html').render(ctx)
                msg = EmailMessage(
                    'Subject',
                    message,
                    'settings.EMAIL_HOST_USER',
                    ['shahidkhan501112@gmail.com'],
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
                print("Mail successfully sent")
            except:
                print("Mail not sent")
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'shop/contractus.html')


@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "age", 'city', "address", 'zipcode', "status", "gender", "phone_no", "description", "pic"]


@method_decorator(login_required, name="dispatch")
class MyProfileDetailView(DetailView):
    model = MyProfile


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'shop/signup.html')
#     else:
# fname = request.POST.get('fname')
# lname = request.POST.get('lname')
# email = request.POST.get('email')
# passd = request.POST.get('pass')
# customer = Customer(f_name=fname,
#                     l_name=lname,
#                     email=email,
#                     password=passd)
# customer.password = make_password(customer.password)
# customer.register()
# return redirect("login")


# def login(request):
#     if request.method == "GET":
#         return render(request, 'shop/login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#
#         error_message = None
#         if(customer):
#             flag = check_password(password , customer.password)
#             if(flag):
#                 request.session['cname'] = customer.email
#                 request.session['c_id'] = customer.id
#                 # print('you are' , request.session.get('cname'))
#                 return redirect("ShopHome")
#             else:
#                 error_message = "Please enter correct username or password !!"
#                 return render(request ,'shop/login.html', {'error' :error_message})
#         else:
#             error_message = "Please enter correct username or password !!"
#             return render(request , 'shop/login.html' , {'error' :error_message})

#
# def cart(request):
#     if request.method == "POST":
#         x1 = request.POST['pidd'];
#         print("==============================")
#         prod = Product.objects.filter(id=x1)
#         print(prod)
#         print("==============================")
#         return render(request, 'shop/cart.html', {"product": prod})
#     return render(request, 'shop/cart.html')


def product_detail(request):
    item = "False"
    if request.method == "POST":
        x = request.POST['nam']
        prod = Case.objects.get(id=x)
        item = cart.objects.filter(Q(product=prod.id) & Q(person=request.user)).exists()
    return render(request, 'shop/product-detail.html', {"pod": prod, 'item': item})


def product_disc(request):
    item = "False"
    if request.method == "POST":
        x = request.POST['nam']
        prod = Product.objects.get(id=x)
        item = cart.objects.filter(Q(product=prod.id) & Q(person=request.user)).exists()
    return render(request, 'shop/product-detail.html', {"pod": prod, 'item': item})


@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    use = request.user.id
    usr = User.objects.get(id=use)
    product = Product.objects.get(id=id)
    xx = cart(person=usr, product=product)
    xx.save()
    return redirect('/showcart/')


@login_required(login_url='/accounts/login/')
def show_cart(request):
    use = request.user.id
    usr = User.objects.get(id=use)
    data = cart.objects.filter(person=usr)
    print(data)

    amount = 0.0
    shipping_amount = 30.0
    total_amount = 0.0
    cart_products = [p for p in cart.objects.all() if p.person == usr]
    if cart_products:
        for i in cart_products:
            tempamount = (i.product.price * i.quantity)
            amount += tempamount
            total_amount = amount + shipping_amount

        d = {'data': data, 'amount': amount, 'total': total_amount, 'ship': shipping_amount}
        return render(request, 'cart/addtocart.html', d)
    else:
        return render(request, 'cart/empty-cart.html')


def plus_cart(request):
    if request.method == 'GET':
        p_id = request.GET['prod_id']
        print(p_id)
        c = cart.objects.get(Q(product=p_id) & Q(person=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 30.0
        total_amount = 0.0
        cart_products = [p for p in cart.objects.all() if p.person == request.user]

        for i in cart_products:
            tempamount = (i.product.price * i.quantity)
            amount += tempamount
            total_amount = amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total': total_amount + shipping_amount
        }

    return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        p_id = request.GET['prod_id']
        print(p_id)
        c = cart.objects.get(Q(product=p_id) & Q(person=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 30.0
        total_amount = 0.0
        cart_products = [p for p in cart.objects.all() if p.person == request.user]

        for i in cart_products:
            tempamount = (i.product.price * i.quantity)
            amount += tempamount
            total_amount = amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total': total_amount + shipping_amount
        }

    return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        p_id = request.GET['prod_id']
        print(p_id)
        c = cart.objects.get(Q(product=p_id) & Q(person=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 30.0
        total_amount = 0.0
        cart_products = [p for p in cart.objects.all() if p.person == request.user]

        for i in cart_products:
            tempamount = (i.product.price * i.quantity)
            amount += tempamount
            total_amount = amount

        data = {

            'amount': amount,
            'total': total_amount + shipping_amount
        }

    return JsonResponse(data)


def check_out(request):
    usr = request.user
    x = MyProfile.objects.get(user=usr)
    cartx = cart.objects.filter(person=usr)
    amount = 0.0
    shipping_amount = 30.0
    total_amount = 0.0
    cart_products = [p for p in cart.objects.all() if p.person == request.user]

    for i in cart_products:
        tempamount = (i.product.price * i.quantity)
        amount += tempamount
        total_amount = amount

    d = {"totalamount": total_amount, "add": x, "cart": cartx}
    return render(request, 'cart/checkout.html', d)


def payment(request):
    usr = request.user
    x = cart.objects.filter(person=usr)
    for c in x:
        orderplaced(user=usr, product=c.product, quantity=c.quantity).save()
        c.delete()

    return redirect('/orders/')


def orders(request):
    usr = request.user
    x = orderplaced.objects.filter(user=usr)

    amount = 0.0
    shipping_amount = 30.0
    total_amount = 0.0
    cart_products = [p for p in orderplaced.objects.all() if p.user == request.user]

    for i in cart_products:
        tempamount = (i.product.price * i.quantity)
        amount += tempamount
        total_amount = amount
    print(total_amount)
    d = {'orders': x, 'total': total_amount}

    return render(request, 'cart/orders.html', d)


# ////////////////////build//////////////

def build_cpu(request):
    data = CPU.objects.all()
    d = {'data1': data}
    return render(request, 'build/cpu.html', d)


def build_home(request):
    dat = ""

    if request.method == 'POST':
        cpu_id = request.POST['cid']
        cpu_nam = request.POST['nammm']
        try:
            dat = CPU.objects.get(cpu_name=cpu_nam)
        except:
            return HttpResponse("cpu does not exixrs")
        chip = dat.chipset.all()
        # equipment = [chip.id for chip in dat.objects.all()]

        request.session['socket'] = dat.socket.socket_type
        request.session['cpuname'] = dat.cpu_name

        li = []
        for d in chip:
            li.append(d.cpu_chipset)

        request.session['listt'] = li

    return render(request, 'shop/build.html')


def build_mobo(request):
    if request.method == 'POST':
        id = request.POST['midd']
        print("//////////////////////")
        print(id)
        sm = Motherboard.objects.get(id=id)
        request.session['moboname'] = sm.mobo_name
        xx = sm.Storage_Interface.all()
        lis = []
        for d in xx:
            lis.append(d.storage_type)

        request.session['lis'] = lis

        ff = sm.Form_Factor
        sram = sm.Supported_ram
        smhz = sm.max_mhz
        x16 = sm.Expensions_socket_version
        request.session['form-factor'] = ff
        request.session['supported_ram'] = sram
        request.session['supported_mhz'] = smhz
        request.session['graphiccard_version'] = x16

        return redirect('/buildhome/')

    print("xxxxxxxxxxxxxxxxx")
    try:
        x = request.session['listt']
        y = request.session.get('socket')
    except:
        x = ""
        y = ""
    # print(x)
    # print(y)
    try:
        xxi = Motherboard.objects.filter(Q(socket__socket_type__exact=y) & Q(chipset__cpu_chipset__in=x))
    except:
        return redirect('/4o4/')

    print(xxi)
    dx = {'data1': xxi}
    return render(request, 'build/mobo.html', dx)


def build_ram(request):
    if request.method == "POST":
        rname = request.POST['rname']
        request.session['ramname'] = rname
        return redirect('/buildhome/')

    x = request.session.get('supported_ram')
    y = request.session.get('supported_mhz')

    dram = Ram.objects.filter(Q(type__exact=x) & Q(mhz__exact=y))

    dx = {'data1': dram}
    return render(request, 'build/ram.html', dx)


def build_Graphicx(request):
    if request.method == 'POST':
        id = request.POST['gid']
        try:
            x = Graphic_Card.objects.get(id=id)
            request.session['gname'] = x.name
            request.session['gpu_power'] = x.recommended_watt
            return redirect('/buildhome/')
        except:
            raise Http404("Gpu does not exist")

    x = request.session.get('supported_ram', '')
    y = request.session.get('supported_mhz', '')
    z = request.session.get('graphiccard_version', '')

    graphic = Graphic_Card.objects.filter(version__iexact=z)

    dx = {'data1': graphic}
    return render(request, 'build/graphiccard.html', dx)


def build_Storage(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        dname = request.POST['dnam']
        request.session['dnam'] = dname
        request.session['ssid'] = sid
        return redirect('/buildhome/')
    data1 = ""
    stog = ""
    print("Hooooooooooooooooo")
    try:
        stog = request.session.get('lis', '')
        print(stog)
    except:
        data1 = Storage.objects.all()

    data1 = Storage.objects.filter(storage_type__in=stog)
    dx = {'data1': data1}
    return render(request, 'build/storage.html', dx)


def build_Psu(request):
    if request.method == "POST":
        x1 = request.POST['pname']
        request.session['psuu'] = x1
        print(request.session['psuu'])
        return redirect('/buildhome/')
    w = request.session.get('gpu_power', '')
    print('xxxxxxxxxxxxxxxxxx')
    print(w)
    data1 = Smps.objects.filter(watt__gte=w)
    data2 = Smps.objects.all()
    print(data1)
    print(data2)
    dx = {'data1': data1}
    return render(request, 'build/Psu.html', dx)


def build_Cases(request):
    if request.method == "POST":
        cid = request.POST['cidd']
        ci = Case.objects.get(id=cid)
        scid = ci.name
        request.session['case'] = scid
        return redirect('/buildhome/')

    else:
        cs = ""
        ffs = request.session.get('form-factor', '')
        print('zxzxzxzxzx')
        print(ffs)
        try:
            cs = Case.objects.filter(Form_Factor=ffs)
        except:
            cs = Case.objects.all()
    dx = {'data1': cs}
    return render(request, 'build/case.html', dx)


def delx(request):
    if request.session['socket']:
        del request.session['socket']

    try:

        del request.session['cpuname']
        del request.session['listt']
        del request.session['lis']
        del request.session['ramname']

        del request.session['psuu']

        del request.session['gname']

        del request.session['dnam']

        del request.session['form-factor']

        del request.session['supported_ram']

        del request.session['case']

        del request.session['supported_mhz']

        del request.session['graphiccard_version']

        del request.session['moboname']

        del request.session['gpu_power']
    except:
        messages.error(request, 'please first select all')
    return redirect('/buildhome/')


def delcpu(request):
    try:
        del request.session['cpuname']
    except:
        messages.warning(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delmobox(request):
    try:
        del request.session['moboname']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delramx(request):
    try:
        del request.session['ramname']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delgraphicx(request):
    try:
        del request.session['gname']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delstoragex(request):
    try:
        del request.session['dnam']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delpowerx(request):
    try:
        del request.session['psuu']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def delcasex(request):
    try:
        del request.session['case']
    except:
        messages.error(request, 'thera is something wrong .')
    return redirect('/buildhome/')


def save_build(request):
    own = request.user.id
    usr = User.objects.get(id=own)
    motherbord = request.session.get('moboname', '')
    ramx = request.session.get('ramname', '')
    graphicc = request.session.get('gname', '')
    storagee = request.session.get('dnam', '')
    psu = request.session.get('psuu', '')
    chases = request.session.get('case', '')
    cpux = request.session.get('cpuname', '')
    xz = CPU.objects.get(cpu_name=cpux)
    img = xz.image
    try:
        xx = Case.objects.get(name=chases)
        im = xx.image
        Build_PC.objects.create(image=im, owner=usr, cpu=cpux, Mobo=motherbord, ram=ramx, graphiccard=graphicc,
                                storage=storagee,
                                power_supply=psu, Chases=chases)
        delx(request)
        return redirect('/')
    except:
        return HttpResponse("There is something wrong in saving your build please correct or contact us")
    return redirect('/')


# /////////////userdashbord//////////////

@login_required(login_url="/accounts/login/")
def usr_dashbord(request):
    return render(request, 'build/bloghome.html')


@login_required(login_url="/accounts/login/")
def usr_builds(request):
    idxx = request.user.id
    dx = User.objects.get(id=idxx)
    data = Build_PC.objects.filter(owner=dx)
    d = {'data': data}
    return render(request, 'build/mybuilds.html', d)


def buy_builds(request, id):
    dat = Build_PC.objects.get(id=id)
    x = CPU.objects.get(cpu_name=dat.cpu)
    y = Motherboard.objects.get(mobo_name=dat.Mobo)
    z = Ram.objects.get(name=dat.ram)
    z1 = Graphic_Card.objects.filter(name=dat.graphiccard).order_by().first()
    print(z1)
    z2 = Smps.objects.get(name=dat.power_supply)
    z3 = Storage.objects.get(name=dat.storage)
    z4 = Case.objects.get(name=dat.Chases)
    p1 = int(x.cpu_price)
    p2 = int(y.price)
    p3 = int(z.price)
    p4 = int(z1.price)
    p5 = int(z2.price)
    p6 = z3.price
    p7 = int(z4.price)
    total = p1 + p2 + p3 + p4 + p5 + p6 + p7
    print("///////////////")
    # p6=int(p6)
    # print(type(p6))
    print(p1, p2, p3, p4, p5, p6, p7)
    print(total)
    d = {'product': dat, 'total': total}
    return render(request, 'cart/build-recipt.html', d)


@login_required(login_url="/accounts/login/")
def del_userbuilds(request, id):
    Build_PC.objects.filter(id=id).delete()
    return redirect('/usrbuilds/')


@login_required(login_url="/accounts/login/")
def blog_Home(request):
    return render(request, 'build/bloghome.html', {'pic': p})


@login_required(login_url="/accounts/login/")
def user_blogg(request):
    cat = Catagory.objects.all()
    author = ""
    d = ""
    if request.method == "POST":
        nam = request.POST['uname']
        cato = request.POST['catagox']
        tit = request.POST['title']
        dat = request.POST['date']
        slg = request.POST['slug']
        img = request.FILES['image']
        stat = request.POST['status']
        cont = request.POST['content']
        print(nam, tit, dat, slg, img, stat, cont)
        z1 = request.user.id
        author = User.objects.get(id=z1)
        raj = Catagory.objects.get(id=cato)
        print(raj)
        p1 = post(title=tit, author=author, catagory=raj, slug=slg, thumbnail=img, status=stat, content=cont)
        p1.save()
        return redirect('/bloghomee/')

    x1 = request.user.id
    x3 = User.objects.get(id=x1)
    print('........')
    print(x3)
    d = {'data': x3, 'cat': cat}

    return render(request, 'build/createblog.html', d)


@login_required(login_url="/accounts/login/")
def user_bloglist(request):
    idd = request.user.id
    xdd = User.objects.get(id=idd)
    data = post.objects.filter(author=xdd)
    d = {'data': data}
    return render(request, 'build/bloglist.html', d)


# vendor signup=========

def vendor_signup(request):
    if request.method == "POST":
        f2 = vendorx(request.POST, request.FILES)
        f1 = VendorUserForm(request.POST)
        if f2.is_valid() and f1.is_valid():
            user = f1.save()
            user.set_password(user.password)
            user.save()
            vendor = f2.save(commit=False)
            vendor.user = user

            vendor = vendor.save()
            my_vendor_group = Group.objects.get_or_create(name='vendor')
            my_vendor_group[0].user_set.add(user)
        else:
            messages.error(request, 'there is something wrong')

            return redirect('/vendor-sign/')
        messages.success(request, 'your are signup successfully wait for admin approve')
        return HttpResponseRedirect('/')

    x = vendorx()
    y = VendorUserForm()
    return render(request, 'shop/vendor.html', {'form': x, 'formu': y})


def delbl(request, id):
    try:
        post.objects.get(post_id=id).delete()
        messages.success(request, "successfully deleted")
        return redirect('/viewblog/')
    except:
        messages.error("Problem in blog deletion")
