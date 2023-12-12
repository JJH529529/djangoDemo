from django.shortcuts import render,HttpResponse
from . import spider,spider_gupiao
from app01.models import Country
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def update_spider(request):
    spider.my_spider()
    # 查询数据库获取更新的数据条数
    num_records_updated = Country.objects.count()

    # 查询数据库获取更新时间
    update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render(request, 'update_success.html', {
        'num_records_updated': num_records_updated,
        'update_time': update_time
    })
def run_spider(request):
    # print(['python', 'spider.py'])

    data_option = request.GET.get('data_option')
    # return render(request, spider.show_csv())
    return render(request,spider.show_csv(data_option))

def run_stock(requset):
    spider_gupiao.spider_gupiao()
    data_category = requset.GET.get('data_category')

    return render(requset,spider_gupiao.visualize_category(data_category))

def visualize_stock_data(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stockName')
        print(stock_name)
        return render(request,spider_gupiao.visualize_stock_data(stock_name) )