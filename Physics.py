def  Collide(obj1, obj2):
    if (obj2.x<obj1.x+obj1.width and
        obj2.x+obj2.width>obj1.x and
        obj2.y>obj1.y-obj1.height and
        obj2.y-obj2.height<obj1.y):
        return True
    else:
        return False

    
