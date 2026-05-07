# -*- coding: utf-8 -*-

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        pass

class NormalItemUpdater(ItemUpdater):
    def update(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 1

class AgedBrieUpdater(ItemUpdater):
    def update(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            if self.item.quality < 50:
                self.item.quality += 1

class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass

class BackstagePassUpdater(ItemUpdater):
    def update(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11:
                if self.item.quality < 50:
                    self.item.quality += 1
            if self.item.sell_in < 6:
                if self.item.quality < 50:
                    self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

class ConjuredItemUpdater(ItemUpdater):
    def update(self):
        self.item.quality -= 2
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality -= 2
        if self.item.quality < 0:
            self.item.quality = 0

class UpdaterFactory:
    registry = {
        "Aged Brie": AgedBrieUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater,
        "Conjured Mana Cake": ConjuredItemUpdater
    }

    @classmethod
    def get_updater(cls, item):
        updater_class = cls.registry.get(item.name, NormalItemUpdater)
        return updater_class(item)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = UpdaterFactory.get_updater(item)
            updater.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
