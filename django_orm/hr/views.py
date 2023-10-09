from django.shortcuts import render
from models import Parser_content


# >>> from blog.models import Blog
# >>> b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
# >>> b.save()


a = Parser_content(message_id=23, message_details='#gotomessage23',title='23.08.2004', from_name='Borya', replied_message_id=21, replied_message_details='#goto21',text='iuu | vayaa', content='puty/istinnogo/samuraya', joined=True)
a.save()