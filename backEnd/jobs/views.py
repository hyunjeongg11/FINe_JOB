import requests
import datetime
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import JobInfoSerializer

allPage = 3
keywords = ['IT', '서비스', '금융', '보험', '인사', '노무', '회계', '세무', '재무', '디자인', '생산', '영업', '상품기획', '교육', 'R&D', '의료', '건축', '전기', '기계', '고객상담', '운송', '미디어', '스포츠', '복지']

# superuser일 때 추가
@api_view(['GET'])
def get_job_info(request): # 사람인 크롤링
    # https://www.saramin.co.kr/zf_user/search?searchType=auto&searchword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage=1&recruitSort=accuracy&recruitPageCount=50&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=y

    for keyword in keywords:
        for page in (1, int(allPage)+1):
            soup = requests.get('https://www.saramin.co.kr/zf_user/search?searchType=auto&searchword={}&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={}&recruitSort=accuracy&recruitPageCount=50'.format(keyword, page), headers={'User-Agent': 'Mozilla/5.0'})
            html = BeautifulSoup(soup.text, 'html.parser')
            jobs = html.select('div.item_recruit')

            for job in jobs:
                try:
                    title = job.select_one('a')['title'].strip().replace(',', '')
                    company = job.select_one('div.area_corp > strong > a').text.strip().replace(',', '')
                    url = 'https://www.saramin.co.kr' + job.select_one('a')['href']
                    deadline = job.select_one('span.date').text.strip()
                    location = job.select('div.job_condition > span')[0].text.strip()
                    experience = job.select('div.job_condition > span')[1].text.strip()
                    requirement = job.select('div.job_condition > span')[2].text.strip()
                    jobtype = job.select('div.job_condition > span')[3].text.strip()
                    # print(today, title, company, url, deadline, location, experience, requirement, jobtype)
                    
                    save_data = {
                        'keyword': keyword,
                        'title': title,
                        'company': company,
                        'url': url,
                        'deadline': deadline,
                        'location': location,
                        'experience': experience,
                        'requirement': requirement,
                        'jobtype': jobtype,
                    }

                    serializer = JobInfoSerializer(data=save_data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()

                except Exception:
                    pass
    return Response({'msg': 'load complete'}, status=status.HTTP_200_OK)