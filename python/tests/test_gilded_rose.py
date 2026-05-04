# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose

def test_normal_item_before_sell_date():
    items = [Item("Normal Item", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 19

def test_normal_item_on_sell_date():
    items = [Item("Normal Item", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 18

def test_normal_item_after_sell_date():
    items = [Item("Normal Item", -1, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -2
    assert items[0].quality == 18

def test_normal_item_quality_never_negative():
    items = [Item("Normal Item", 10, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 0

def test_aged_brie_before_sell_date():
    items = [Item("Aged Brie", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 21

def test_aged_brie_after_sell_date():
    items = [Item("Aged Brie", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 22

def test_aged_brie_quality_never_exceeds_50():
    items = [Item("Aged Brie", 10, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 50

def test_sulfuras_never_changes():
    items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80

def test_backstage_passes_more_than_10_days():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 14
    assert items[0].quality == 21

def test_backstage_passes_10_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 22

def test_backstage_passes_5_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4
    assert items[0].quality == 23

def test_backstage_passes_after_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 0
