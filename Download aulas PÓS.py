from logging import exception
import requests
import re
import sys
import os


lessons = {
            "Introdução à Ciência de Dados e à Inteligência Artificial" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/513920520?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/513937612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/513954413?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/513973389?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/514264039?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/514278493?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/514291086?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/514309571?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/514437686?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/514449649?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/514461613?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/514478849?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Fundamentos de Estatística para Ciência de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/519548558?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/521456379?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/521529605?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/522951506?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/521469486?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/521489720?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/521556791?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/521571433?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/521896223?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/521916595?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/521932612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/521954689?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/522365274?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/522380023?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/522392650?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/522402609?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/522884500?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/522903875?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/522924072?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/522941675?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/522440585?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/522986959?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/522992903?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/522998336?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Python para Ciência de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/531323095?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/531472102?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/531487322?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/531498586?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/531505124?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/531513757?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/531542267?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/531548078?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/531557297?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/531562918?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/531534958?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/531568628?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/531574053?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/531583516?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/531544379?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/531545661?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/531547264?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/531548686?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/531560887?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/531562211?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/531563210?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/531564726?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Bancos de Dados Relacionais e Não-Relacionais" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/538738478?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/538752876?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/538764630?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/538782663?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/537766304?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/537774950?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/537790562?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/537861821?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/538789669?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/538796384?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/538802589?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/538813810?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/538838479?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/538850516?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/538858334?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/538868244?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/538878232?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/538893077?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/538906491?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/538912584?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/538918727?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/538928482?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/538936396?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/538945120?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Pré-processamento de Dados" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/545315382?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/545311483?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/545332196?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/545322176?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/545340200?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/545345467?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/545444200?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/545449776?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/544807823?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/544832612?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/544838172?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/544845949?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/545221056?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/545237681?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/545250182?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/545267086?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/545268885?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/567656057?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/545272473?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/565411515?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/545285657?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/545294419?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/545288375?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Gerência de Infraestrutura para Big Data" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/554421362?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/554562026?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/554482630?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/554490328?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/554580058?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/554590849?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/554596669?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/554502984?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/554510465?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/554514501?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/554543999?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/554532950?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/554542357?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/554556869?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/554619647?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/554551410?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/554558203?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/554670600?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/554676491?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/554566113?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/554664430?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/554667061?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/554661769?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Inteligência de Negócio" : {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/569930900?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/569953801?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/570004130?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/570016512?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/570025945?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/570039712?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/570104721?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/570151014?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/570515723?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/570502002?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/570525354?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/570542221?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/584111485?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/570562983?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/570566576?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/570649711?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/570658373?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/570681867?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/570696533?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/570708176?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/570731973?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 5" : "https://player.vimeo.com/video/570742985?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Machine Learning I Aprendizado suprvisionado": {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/645798194?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/646220747?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/646228513?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/646239485?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 5" : "https://player.vimeo.com/video/646246969?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/646226275?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/646234092?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/646239920?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/646244844?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/646250341?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/646255742?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/646257362?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/646260084?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/646259572?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/646263732?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/645857207?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/645890777?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/646215568?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/646269018?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/646273380?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/646280221?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/646269070?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 5" : "https://player.vimeo.com/video/646273167?api=1&player_id=vimeoAula&autoplay=1",
                "Aula Extra" : "https://player.vimeo.com/video/682000698?api=1&player_id=vimeoAula&autopause=0"
            },

            "Deep Learning I Redes Neurais para Visão computacional" :{
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/651247429?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/651254651?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/651295361?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/651300091?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/651310293?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/651312096?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/651318263?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/651304357?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/651325997?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/651333455?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/651338994?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/651344373?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/651347881?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/651350662?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/651300403?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/651306028?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/651304205?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/651310361?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/651320366?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/651334798?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/651324817?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/651329038?api=1&player_id=vimeoAula&autoplay=1",
                "Aula Extra"     : "https://player.vimeo.com/video/691238482?api=1&player_id=vimeoAula&autopause=0"
            },

            "Deep Learning II Redes Neurais para Processamento de linguagem natual": {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/656511910?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/656514578?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/656517535?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/656520795?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/656554008?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/656563875?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/656577736?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/656584084?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/656606729?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/656611699?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/656679712?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/656684705?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/656717600?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/656724746?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/656730939?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 5" : "https://player.vimeo.com/video/656736567?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/656759993?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/656765113?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/656779671?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/656785568?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/656795656?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/656800864?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/656814338?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/656824250?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Visualização de Dados": {
                "Aula 1 Parte 1" : "https://player.vimeo.com/video/691238482?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/666051963?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/666078332?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/666126562?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/666200300?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/666194883?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/666184441?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/666203985?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/666131748?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/666133221?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/676494215?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/676506328?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/676510915?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/666148916?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/666156329?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/666203685?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/666207031?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 5" : "https://player.vimeo.com/video/666217145?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/666219747?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/666222540?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/666227062?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/666227638?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 7 Parte 1" : "https://player.vimeo.com/video/676574068?api=1&player_id=vimeoAula&autopause=0",
                "Aula 7 Parte 2" : "https://player.vimeo.com/video/676577337?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 7 Parte 3" : "https://player.vimeo.com/video/676578543?api=1&player_id=vimeoAula&autoplay=1"
            },

            "Machine Learning II Aprendizado não supervisionado": {

                "Aula 1 Parte 1" : "https://player.vimeo.com/video/677878126?api=1&player_id=vimeoAula&autopause=0",
                "Aula 1 Parte 2" : "https://player.vimeo.com/video/677895120?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 3" : "https://player.vimeo.com/video/677931265?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 1 Parte 4" : "https://player.vimeo.com/video/677938934?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 1" : "https://player.vimeo.com/video/677969262?api=1&player_id=vimeoAula&autopause=0",
                "Aula 2 Parte 2" : "https://player.vimeo.com/video/677982200?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 3" : "https://player.vimeo.com/video/677998503?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 2 Parte 4" : "https://player.vimeo.com/video/678304089?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 1" : "https://player.vimeo.com/video/678153253?api=1&player_id=vimeoAula&autopause=0",
                "Aula 3 Parte 2" : "https://player.vimeo.com/video/690750615?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 3" : "https://player.vimeo.com/video/678163047?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 3 Parte 4" : "https://player.vimeo.com/video/678166988?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 1" : "https://player.vimeo.com/video/679288371?api=1&player_id=vimeoAula&autopause=0",
                "Aula 4 Parte 2" : "https://player.vimeo.com/video/679342517?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 3" : "https://player.vimeo.com/video/679344006?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 4 Parte 4" : "https://player.vimeo.com/video/679345023?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 1" : "https://player.vimeo.com/video/679773978?api=1&player_id=vimeoAula&autopause=0",
                "Aula 5 Parte 2" : "https://player.vimeo.com/video/679392396?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 3" : "https://player.vimeo.com/video/679393194?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 5 Parte 4" : "https://player.vimeo.com/video/679505358?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 1" : "https://player.vimeo.com/video/679558746?api=1&player_id=vimeoAula&autopause=0",
                "Aula 6 Parte 2" : "https://player.vimeo.com/video/679559351?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 3" : "https://player.vimeo.com/video/679559896?api=1&player_id=vimeoAula&autoplay=1",
                "Aula 6 Parte 4" : "https://player.vimeo.com/video/679560611?api=1&player_id=vimeoAula&autoplay=1"
            }


        }


headers = {'Referer': 'https://salavirtual.pucrs.br/'}




def create_directory(dirName):
    try:
        os.makedirs(dirName)    
        print("[+] Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("[-] Directory " , dirName ,  " already exists")  






def parser(input, option):
    
    regex = r'"profile":"\d+","width":\d+,"height":\d+,"mime":"video/mp4","fps":\d+\.\d+,"url":"(https.+?)","cdn":"akamai_interconnect","quality":"(.+?)",'
    matches = re.finditer(regex, input)
    for matchNum, match in enumerate(matches, start=1):
        if match.group(2) == option:
            return match.group(1)





def download(link, x):
    print(link)
    file_name = f"{x}.mp4"
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        try:
            response = requests.get(link, stream=True, headers=headers)
            total_length = response.headers.get('content-length')
            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
        except ConnectionError:
            print("\n[-] Não conectou ao site, verifique a conexão e execute o script novamente")


         

             
         

def menu_video():
    option = -1
    op = ['1080p', '720p', '540p', '360p', '240p']
    while option not in range(0,5):
        print("\n\nSelect Video Quality:\n0. 1080p\n1. 720p\n2. 540p\n3. 360p\n4. 240p\n")
        option = int(input("Option: "))
        
    return op[option]


def menu_lessons():
    x = 0
    loption = -1
    print("\n\nSelect Lesson: ")
    for lesson, lessonData in lessons.items():
        print(f"{x} - {lesson}")
        x = x + 1
    while loption not in range(0,x):
        loption = int(input("Option: "))
    return loption


option = menu_video()
loption = menu_lessons()
x = 0


for lesson, lessonData in lessons.items():
    if x == loption:
        print(f"\n\n{lesson}")
        if not os.path.isdir(f"./{lesson}"):
            create_directory(f"./{lesson}")
        for lessonName, link in lessonData.items():
            if not os.path.exists(f"./{lesson}/{lessonName}.mp4"):
                print(f"\n[+] Accessing {link}")
                try:
                    r = requests.get(link, headers=headers, allow_redirects=True).text
                except ConnectionError:
                    print("\n[-] Não conectou ao site, verifique a conexão e execute o script novamente")

                html = r
                link_mp4 = parser(html, option)
                download(link_mp4, f"./{lesson}/{lessonName}")
    x = x + 1
