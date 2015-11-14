def  Collide(obj1, obj2):
    if (obj2._position.x<obj1._position.x+obj1._width and
        obj2._position.x+obj2._width>obj1._position.x and
        obj2._position.y>obj1._position.y-obj1._height and
        obj2._position.y-obj2._height<obj1._position.y):
        return True
    else:
        return False

    
