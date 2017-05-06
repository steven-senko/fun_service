import requests
from lxml import html
import boto3
from botocore.exceptions import ClientError

from chalice import Chalice, Response

app = Chalice(app_name='fun_service')
S3 = boto3.client('s3', region_name='us-east-1')
BUCKET = 'fun-service'

def check_parenthesis(text):
    """
    This method returns True if all opening parenthesis
    are matched by closing parenthesis
    otherwise
    it returns False
    """
    chars = list(text)
    temp = []

    for c in chars:

        if c == "(":
            temp.append(c)
        elif c == ")":

            if temp:
                if temp[-1] == "(":
                    temp.pop()
                else:
                    temp.append(c)
            else:
                pass

    return False if temp else True


def follow_links(seen):
    """
    This method crawls through the first links on the pages
    it can find
    If Wikipedia server returns status not equal to 200
    method returns an empty path
    If method can not find a link it returns an empty path
    """
    if not seen:
        return []

    def get_title(s):
        response = requests.get(
            u"https://en.wikipedia.org/w/index.php?action=render&title={0}".format(s.replace(u" ", u"%20")))

        if response.status_code == 200:
            page = html.fromstring(response.content)
            tables = page.xpath('//table')

            for table in tables:  # Removing all tables to avoid interference while finding useful links
                table.getparent().remove(table)

            paragraphs = page.xpath('//p')
            paragraphs.extend(page.xpath('//li'))
            for paragraph in paragraphs:

                for i in range(len(paragraph)):
                    tag = paragraph[i].tag

                    if tag == "b":
                        temp = html.tostring(paragraph[i])

                        if '<a' in temp:  # If a link is wrapped in the <b> tag, then unwrapping it
                            start = temp.index('<a')
                            end = temp.index('</a>') + 4
                            temp = ''.join(list(temp)[start:end])
                            paragraph[i] = html.fromstring(temp)
                            tag = 'a'

                    article = paragraph[i].get('title')
                    href = paragraph[i].get('href')

                    if tag == "a" and article is not None and not href.startswith('http'):

                        before_link = " ".join(map(html.tostring, paragraph[:i]))
                        is_good = True

                        if before_link and "(" in before_link:
                            is_good = check_parenthesis(before_link)
                        if is_good:
                            return article
        return False

    while seen[-1] != "Philosophy":
        # print(seen[-1])
        title = get_title(seen[-1])
        if title and title not in seen:
            seen.append(title)
        else:
            return []

    return seen


@app.route('/')
def index():
    return {'status': 'ok'}


@app.route('/wiki/{article_name}')
def wiki(article_name):
    res = follow_links([article_name])
    return {'path': res}


@app.route('/png/{key}', methods=['GET', 'PUT'],
           content_types=['image/png'])
def png(key):
    request = app.current_request
    if request.method == 'PUT':
        S3.put_object(Bucket=BUCKET, Key=key + '.png',
                      Body=request.raw_body,
                      ContentType='image/png')

        return Response(body=request.raw_body,
                        status_code=200,
                        headers={'Content-Type': 'image/png'})
    elif request.method == 'GET':
        try:
            body = S3.get_object(Bucket=BUCKET, Key=key + '.png')
            return Response(body=body['Body'].read(),
                    status_code=200,
                    headers={'Content-Type': 'image/png'})
        except ClientError:
            raise Chalice.NotFoundError(key)

