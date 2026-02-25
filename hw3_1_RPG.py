class Item():
    ibase= []
    def __init__(self, iname, itype, weight, cost, ibase=ibase):
        self.iname = iname
        self.itype = itype
        self.weight = weight
        self.cost = cost
        ibase.append(self)
        print(f'Предмет {self.iname} добавлен в базу')
    def use(self, player:Player):
        player.inventory.remove(self)
        player.weight += self.weight
        print(f'Предмет {self.iname} успешно использован')
    def description(self):
        return {
        'name' : self.iname,
        'type' : self.itype,
        'weight' : self.weight,
        'cost' : self.cost
        }


class Player():
    def __init__(self, pname, hp:int, max_weight, money):
        self.pname = pname
        self.hp = hp
        self.inventory = []
        self.weight = max_weight
        self.money = money
        print(f'Игрок {self.pname} добавлен в базу')
    def pickup(self, item:Item):
        if self.weight>=item.weight:
            self.inventory.append(item)
            self.weight -= item.weight
            print(f'Предмет {item.iname} добавлен в инвентарь игрока {self.pname}')
        else:
            print('Недостаточно места в инвентаре')
    def sell(self,item:Item):
        self.inventory.remove(item)
        self.money += item.cost
        print(f'Предмет {item.iname} успешно продан за {item.cost}')
    def show_inv(self):
        for i in self.inventory:
            print(f'{i.description()}\n')

class Inventory():
    def __init__(self, owner:Player):
        self.owner = owner
        self.open = owner.show_inv
        self = owner.inventory
    def add(self, item:Item):
        if self.owner.weight>=item.weight:
            self.append(item)
            self.owner.weight -= item.weight
            print(f'Предмет {item.iname} добавлен в инвентарь игрока {self.owner.pname}')
        else:
            print('Недостаточно места в инвентаре')
    def dump(self, item:Item):
        if item in self:
            self.remove(item)
            self.owner.weight+=item.weight
            print(f'Предмет {item.iname} успешно удален')
        else:
            print('В инвентаре нет такого предмета')
    def finditem(self, itype):
        print(f'Найдены предметы : {[i.name for i in self if i.itype == itype]}')
    def getcost(self):
        print(f'Общая стоимость: {sum([i.cost for i in self])}\n Самый дорогой предмет: {[i.iname for i in self if i.cost == max([i.cost for i in self])]} (Цена: {max([i.cost for i in self])})')
    
    


