# templatetags/blog_utils.py
from django import template
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='add_img_class')
def add_img_class(html: str, classes: str = 'img-fluid'):
    """
    사용: {{ item.body_html|add_img_class:"img-fluid"|safe }}
    여러 클래스: {{ item.body_html|add_img_class:"img-fluid rounded"|safe }}
    """
    if not html:
        return ''
    if BeautifulSoup is None:
        # bs4가 없을 땐 원본 그대로(또는 예외 발생시키도록 바꿔도 됨)
        return html

    soup = BeautifulSoup(html, 'lxml')  # 'html.parser'도 가능하나 lxml 권장
    class_list = [c for c in (classes or '').split() if c]

    for img in soup.find_all('img'):
        current = set(img.get('class', []))
        current.update(class_list)
        if current:
            img['class'] = sorted(current)

    return mark_safe(str(soup))

@register.filter
def remove_images(html: str) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    # 이미지 관련 태그 제거
    for tag in soup.find_all(["img", "figure", "picture", "source"]):
        tag.decompose()
    return str(soup)


