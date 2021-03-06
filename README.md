# fun_service

Before you start:<br/>

<ol>
<li>Sign up for AWS</li>
<li>Create S3 storage</li>
<li>Install aws on your local machine<br/>
http://docs.aws.amazon.com/cli/latest/userguide/installing.html</li>
<li>Install virtualenv on your local machine<br/>
https://www.digitalocean.com/community/tutorials/common-python-tools-using-virtualenv-installing-with-pip-and-managing-packages</li>
</ol>

Run these commands to start the service on AWS:<br/>
```
virtualenv fun_service_venv && cd fun_service_venv
source bin/activate
pip install chalice
chalice new-project fun_service && cd fun_service
git clone https://github.com/steven-senko/fun_service.git
mv fun_service/* .
rm -rf fun_service
pip install -r requirements.txt
```
Edit variables REGION_NAME and BUCKET in the app.py accordingly to your S3 settings<br/>

Run last line:<br/>
```
chalice deploy
```
After executing the previous line you will get a link like this:<br/>
https://lrrtzc6ov0.execute-api.us-east-1.amazonaws.com/dev/<br/>

This is the end-point for the newly created web service<br/>

# fun_service API<br/>

<ul>
<li><b>GET /</b><br/>
returns {'status': 'ok'}</li>
<li><b>GET /wiki/{article_name}</b><br/>
takes article's name as a parameter and looks up it on Wikipedia,<br/>
finds first link in the article's body and follows it.<br/>
returns a JSON object with a list of article's names from the Wikipedia which lead to the Philosophy page<br/>
e.g. {"path": ["programmer", "Computer software", "Computer system", "Computer programming", "Computing", "Mathematics", "Quantity", "Property (philosophy)", "Philosophy"]}<br/>
or an empty list if given article leads to an empty page or creates an infinite loop</li>
<li><b>GET /png/{file_name}</b><br/>
returns a file with a given name from the S3 storage</li>
<li><b>PUT /png/{file_name}</b><br/>
uploads file to the S3 storage and gives it name from parameter</li>
</ul>

# TODO:

The service does not work as expected with .png files and needs a fix