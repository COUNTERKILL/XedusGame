def  Collide(obj1, obj2):
    if (obj2.position.x<obj1.position.x+obj1.width and
        obj2.position.x+obj2.width>obj1.position.x and
        obj2.position.y>obj1.position.y-obj1.height and
        obj2.position.y-obj2.height<obj1.position.y):
        return True
    else:
        return False

    
