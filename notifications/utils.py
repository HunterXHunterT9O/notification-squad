def generate_notification(user, action):
    
    message = user.username
    
    if action == 'CA':
        message += 'created a new announcement'
    elif action == 'LA':
        message += 'liked announcement "Announcement Title"'
    elif action == 'DA':
        message += 'deleted announcement "Announcement Title"'
    elif action == 'CC':
        message += 'created a new comment'
    elif action == 'LC':
        message += 'liked your comment'
    elif action == 'DC':
        message += 'deleted your comment'
    
    return message
