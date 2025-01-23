from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

# 사용자 목록
@login_required(login_url='auth:login')
@user_passes_test(lambda u: u.is_superuser)
def get_users(request):
    return HttpResponse('사용자 목록')

# 사용자 보기
@login_required(login_url='auth:login')
@user_passes_test(lambda u: u.is_superuser)
def get_user(request, user_id):
    return HttpResponse('사용자 보기')

# 사용자 삭제
@login_required(login_url='auth:login')
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    return HttpResponse('사용자 삭제')


# 사용자 목록
@login_required(login_url='auth:login')
@user_passes_test(lambda u: u.is_superuser)
def get_users(request):
    page = request.GET.get('page', '1')
    searchType = request.GET.get('searchType')
    searchKeyword = request.GET.get('searchKeyword')
    users = User.objects.all().order_by('username')

    # 검색 조건 처리
    if searchType not in [None, ''] and searchKeyword not in [None, '']:
        if searchType == 'all':
            users = users.filter(
                Q(username__contains=searchKeyword) |
                Q(first_name__contains=searchKeyword) |
                Q(email__contains=searchKeyword)
            )

    # 페이징네이션
    paginator = Paginator(users, 10)
    page_obj = paginator.get_page(page)

    # 현재 페이지의 첫 번째 사용자 번호 계산
    start_index = paginator.count - (paginator.per_page * (page_obj.number - 1))

    # 순번 계산하여 사용자 리스트에 추가
    for index, u in enumerate(page_obj, start=0):
        page_obj[index].index_num = start_index - index

    return render(request, 'users/list.html', {
        'users': page_obj,
        'searchType': searchType,
        'searchKeyword': searchKeyword
    })
