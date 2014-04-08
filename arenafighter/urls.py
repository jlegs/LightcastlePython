from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arenafighter.views.home.home', name='home'),
    url(r'^store$', 'arenafighter.views.store.shop', {'store_level': 1}, name='store'),
    url(r'^info/(\d+)/$', 'arenafighter.views.home.info', name='player_info'),
    url(r'^arena$', 'arenafighter.views.home.go_to_arena', name='arena'),

    url(r'^store/sell$', 'arenafighter.views.store.character_inventory', name='sell_detail'),

    url(r'^equip/weapon/(\d+)$', 'arenafighter.views.home.equip_weapon', name='equip_weapon'),
    url(r'^equip/armor/(\d+)$', 'arenafighter.views.home.equip_armor', name='equip_armor'),
    url(r'^unequip/weapon/(\d+)$', 'arenafighter.views.home.unequip_weapon', name='unequip_weapon'),
    url(r'^unequip/armor/(\d+)$', 'arenafighter.views.home.unequip_armor', name='unequip_armor'),


    url(r'^item/(\d+)$', 'arenafighter.views.store.potion_detail', name='potion_detail'),
    url(r'^store/item/(\d+)$', 'arenafighter.views.store.potion_detail', {'store': True}, name='store_potion_detail'),
    url(r'^store/sell/item/(\d+)$', 'arenafighter.views.store.sell_potion', name='sell_potion'),
    url(r'^store/buy/item/(\d+)$', 'arenafighter.views.store.purchase_potion', name='purchase_potion'),

    url(r'^weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', name='weapon_detail'),
    url(r'^store/weapon/(\d+)$', 'arenafighter.views.store.weapon_detail', {'store': True}, name='store_weapon_detail'),
    url(r'^store/sell/weapon/(\d+)$', 'arenafighter.views.store.sell_weapon', name='sell_weapon'),
    url(r'^store/buy/weapon/(\d+)$', 'arenafighter.views.store.purchase_weapon', name='purchase_weapon'),

    url(r'^armor/(\d+)$', 'arenafighter.views.store.armor_detail', name='armor_detail'),
    url(r'^store/armor/(\d+)$', 'arenafighter.views.store.armor_detail', {'store': True}, name='store_armor_detail'),
    url(r'^store/sell/armor/(\d+)$', 'arenafighter.views.store.sell_armor', name='sell_armor'),
    url(r'^store/buy/armor/(\d+)$', 'arenafighter.views.store.purchase_armor', name='purchase_armor'),


    url(r'^fight', 'arenafighter.views.arena.fight', name='fight'),
    url(r'^attack$', 'arenafighter.views.arena.attack', name='attack'),

    url(r'^use-potion$', 'arenafighter.views.arena.use_potion', name='use_potion'),



    url(r'^play_as/(\d+)', 'arenafighter.views.home.play_as_character', name='play_as_character'),
    url(r'^delete/(\d+)', 'arenafighter.views.home.delete', name='delete'),
    url(r'^signup/', 'arenafighter.views.home.signup', name='signup'),
    url(r'^login/', 'arenafighter.views.home.log_in', name='log_in'),
    url(r'^logout/', 'arenafighter.views.home.log_out', name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
