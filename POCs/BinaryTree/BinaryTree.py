# Binary Tree
class Btree:
        def __init__(self, root, key):
            self.root = root
            self.key = key
            self.lc = None
            self.rc = None

        def insert_rc(self, newNode):
            if self.rc == None:
                #Parent node is the one the insert_rc method is called on,
                #so we pass self as the root parameter
                self.rc = Btree(self, newNode)
            else:
                t = Btree(self, newNode)
                self.rc = t
        def insert_rc(self, newNode):
                if self.rc == None:
                        self.rc = Btree(newNode)
                else:
                        t = Btree(newNode)
                        t.rc = self.rc
                        self.rc = t

        def get_rc(self):
                return self.rc
        def get_lc(self):
                return self.lc

        def set_Root(self, val):
                self.key = val
        def get_Root(self):
                return self.key




r = Btree(1)
r.insert_lc(2)
r.insert_rc(4)
#Insert left child to the node with key=2
r.get_lc().insert_lc(3)
#Insert right child to the node with key=4
r.get_rc().insert_rc(5)