APPLIST = [
    {
        "title":'Home', 'has_children':False, 'url':'', 'is_active':True, 'icon':'nav-icon ti ti-home', "key":'001', 'children':[]
    },
    
    {
        "title":'Audio', 'has_children':True, 'url':'audio', 'is_active':True, 'icon':'nav-icon ti ti-music', "key":'002', 'children':[
            {'title':'Albums', 'is_active':True, 'url':'audio/album/', 'icon':'', 'has_icon':False},
            {'title':'Genres', 'is_active':True, 'url':'audio/genre/', 'icon':'', 'has_icon':False},
            {'title':'Like songs', 'is_active':True, 'url':'audio/likesong/', 'icon':'', 'has_icon':False},
            {'title':'Playlists', 'is_active':True, 'url':'audio/playlist/', 'icon':'', 'has_icon':False},
            {'title':'Tracks', 'is_active':True, 'url':'audio/track/', 'icon':'', 'has_icon':False}
        ]
    },
    
    {
        "title":'User', 'has_children':True, 'url':'user', 'is_active':True, 'icon':'nav-icon ti ti-user', "key":'003', 'children':[
            {'title':'Custom users', 'is_active':True, 'url':'users/customuser/', 'icon':'', 'has_icon':False},
            {'title':'Artists', 'is_active':True, 'url':'users/artist/', 'icon':'', 'has_icon':False},
            {'title':'Clients', 'is_active':True, 'url':'users/client/', 'icon':'', 'has_icon':False},
            {'title':'Followers', 'is_active':True, 'url':'users/follower/', 'icon':'', 'has_icon':False},
        ]
    },
]