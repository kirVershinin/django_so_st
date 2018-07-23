sudo ln -sf /home/elc/Documents/PyPrac/CoursePrac/Stepik_Web/web_app/etc/nginx.conf  /etc/nginx/
sudo /usr/bin/nginx
#sudo ln -sf $(pwd)/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
gunicorn hello:app -b localhost:8080 &
