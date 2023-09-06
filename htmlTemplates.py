css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.pinimg.com/474x/da/d4/e6/dad4e64354f447e23c6004a04201b329.jpg"></div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1149470815/photo/put-in-the-work-and-youll-reap-the-benefits.jpg?s=612x612&w=0&k=20&c=WfReBTfB5ATGoLshqU_MUzs7_uhA1O4DgspbJ6s4yQI=">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''