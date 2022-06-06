from django.shortcuts import render
from nox import param
from pandas import array
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Equipo, Jugadores, Cuerpo_técnico
from base.serializers import Equipo_serializers, Jugadores_serializers, Cuerpo_técnico_serializers
from datetime import datetime
from dateutil import relativedelta
import numpy as np
from array import array

@api_view(['GET'])
def NEquipos(request):
    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    data=len(Serializer.data)
    return Response({
    'cantidad de equipos': data,
})

@api_view(['GET'])
def allPalyers(request):
    items = Jugadores.objects.all()
    Serializer= Jugadores_serializers(items, many=True)
    data=len(Serializer.data)
    return Response({
    'cantidad de jugadores': data,
})

@api_view(['GET'])
def Youngest(request):
    items = Jugadores.objects.all()
    Serializer= Jugadores_serializers(items, many=True)
    data=Serializer.data
    youngest=100
    for i in range(len(data)):
        try:
            date_1 =  data[i]['Fnacimiento'].strip()
            today = datetime.today()
            date_2 = today.strftime("%d/%m/%Y")
            date_format_str = '%d/%m/%Y' 
            start = datetime.strptime(date_1, date_format_str)
            end =   datetime.strptime(date_2, date_format_str)
            diff = relativedelta.relativedelta(end, start)
            print(diff.years)

            if diff.years<youngest:
                youngest=diff.years
                pos = i
                equipo = data[i]['idEquipo'] 

        except Exception:
            pass 

    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    product = Equipo.objects.get(id=equipo)
    Equiposerializer = Equipo_serializers(product, many=False)

    return Response({
    'El jugador mas joven es': data[pos]['Nombre']+' '+data[pos]['Apellido'],
    'edad': youngest,
    'Juega en': Equiposerializer.data['Nombre_Equipo']
})

@api_view(['GET'])
def oldest(request):
    items = Jugadores.objects.all()
    Serializer= Jugadores_serializers(items, many=True)
    data=Serializer.data
    youngest=0
    for i in range(len(data)):
        try:
            date_1 =  data[i]['Fnacimiento'].strip()
            today = datetime.today()
            date_2 = today.strftime("%d/%m/%Y")
            date_format_str = '%d/%m/%Y' 
            start = datetime.strptime(date_1, date_format_str)
            end =   datetime.strptime(date_2, date_format_str)
            diff = relativedelta.relativedelta(end, start)
            print(diff.years)

            if diff.years>youngest:
                youngest=diff.years
                pos = i
                equipo = data[i]['idEquipo'] 

        except Exception:
            pass 

    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    product = Equipo.objects.get(id=equipo)
    Equiposerializer = Equipo_serializers(product, many=False)

    return Response({
    'El jugador mas viejo es': data[pos]['Nombre']+' '+data[pos]['Apellido'],
    'edad': youngest,
    'Juega en': Equiposerializer.data['Nombre_Equipo']
})

@api_view(['GET'])
def substitute_players(request):
    items = Jugadores.objects.filter(titular='FALSO').order_by('id')
    Serializer= Jugadores_serializers(items, many=True)
    num = len(Serializer.data)
    return Response({
    'El numero de suplentes es': num,
})


@api_view(['GET'])
def average_substitute_each_team(request):

    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    EquiposData = Serializer.data
    teams=[]
    cantPlayer=0

    for i in range(len(EquiposData)):
        items = Jugadores.objects.filter(titular='FALSO',idEquipo=EquiposData[i]['id']).order_by('id')
        SerializerSubstitute= Jugadores_serializers(items, many=True)
        dataSubstitute=SerializerSubstitute.data
        cantPlayer=cantPlayer+len(dataSubstitute)

        items = Jugadores.objects.filter(idEquipo=EquiposData[i]['id']).order_by('id')
        players= Jugadores_serializers(items, many=True)
        data=players.data
        average=0
        if len(data)!=0:
            math=len(dataSubstitute)/len(data)
            average="{0:.1f}%".format(math*100)
      
        teams.append({
            'Equipo': EquiposData[i]['Nombre_Equipo'],
            'Promedio': average,
        })
    
    math=cantPlayer/len(EquiposData)
    average="{0:.1f}".format(math)

    teams.append({
        'Promedio de jugadores suplentes': average,
    })

    return Response(teams)

@api_view(['GET'])
def Number_players(request):

    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    EquiposData = Serializer.data
    cantPlayer=0

    for i in range(len(EquiposData)):
        items = Jugadores.objects.filter(idEquipo=EquiposData[i]['id']).order_by('id')
        SerializerSubstitute= Jugadores_serializers(items, many=True)
        dataSubstitute=SerializerSubstitute.data

        if len(dataSubstitute)>cantPlayer:
            cantPlayer=len(dataSubstitute)

    return Response({
        'Equipo con mayor cantidad de jugadores': EquiposData[i]['Nombre_Equipo'],
        'jugadores': cantPlayer,
    })

@api_view(['GET'])
def average_age(request):
    items = Jugadores.objects.all()
    Serializer= Jugadores_serializers(items, many=True)
    data=Serializer.data
    age=0
    for i in range(len(data)):
        try:
            date_1 =  data[i]['Fnacimiento'].strip()
            today = datetime.today()
            date_2 = today.strftime("%d/%m/%Y")
            date_format_str = '%d/%m/%Y' 
            start = datetime.strptime(date_1, date_format_str)
            end =   datetime.strptime(date_2, date_format_str)
            diff = relativedelta.relativedelta(end, start)
            age=age+diff.years
        except Exception:
            pass 

    math=age/len(data)
    average="{0:.1f}".format(math)

    return Response({
    'El promedio de edad es':average
})

@api_view(['GET'])
def average_players_ByTeam(request):

    items = Equipo.objects.all()
    Serializer= Equipo_serializers(items, many=True)
    EquiposData = Serializer.data
    teams=[]
    cantPlayer=0

    for i in range(len(EquiposData)):
        items = Jugadores.objects.filter(idEquipo=EquiposData[i]['id']).order_by('id')
        players= Jugadores_serializers(items, many=True)
        data=players.data
        average=0

        teams.append({
            'Equipo': EquiposData[i]['Nombre_Equipo'],
            'Numero de jugadores': len(data),
        })

        cantPlayer=cantPlayer+len(data)

    math=cantPlayer/len(EquiposData)
    average="{0:.1f}".format(math)

    teams.append({
        'Promedio de jugadores por Equipo': average,
    })

    return Response(teams)

@api_view(['GET'])
def technical_oldest(request):
    items = Cuerpo_técnico.objects.filter().order_by('id')
    Serializer= Cuerpo_técnico_serializers(items, many=True)
    num = len(Serializer.data)
    oldest=0
    for i in range(len(Serializer.data)):
        try:
            edge=Serializer.data[i]['FNacimiento']
            if oldest<int(edge):
                nombre=Serializer.data[i]['Nombre']
                oldest=edge
        except Exception:
            pass
        
    return Response({
    'El tecnico mas viejo es: ': nombre,
    'conuna dedad de: ': edge,
})


    # items = Cuerpo_técnico.objects.filter(FNacimiento).order_by('id')
    # Serializer= Cuerpo_técnico_serializers(items, many=True)
    # data=Serializer.data
    # youngest=0
    # return data
    # for i in range(len(data)):
    #     try:
    #         date_1 =  data[i]['Fnacimiento'].strip()
    #         today = datetime.today()
    #         date_2 = today.strftime("%d/%m/%Y")
    #         date_format_str = '%d/%m/%Y' 
    #         start = datetime.strptime(date_1, date_format_str)
    #         end =   datetime.strptime(date_2, date_format_str)
    #         diff = relativedelta.relativedelta(end, start)
    #         print(diff.years)

    #         if diff.years>youngest:
    #             youngest=diff.years
    #             pos = i
    #             equipo = data[i]['idEquipo'] 

    #     except Exception:
    #         pass 

    # items = Equipo.objects.all()
    # Serializer= Equipo_serializers(items, many=True)
    # product = Equipo.objects.get(id=equipo)
    # Equiposerializer = Equipo_serializers(product, many=False)

#     return Response({
#     'El jugador mas viejo es': data[pos]['Nombre']+' '+data[pos]['Apellido'],
#     'edad': youngest,
#     'Juega en': Equiposerializer.data['Nombre_Equipo']
# })


# INSERT INTO `base_jugadores` (`id`, `Foto`, `Nombre`, `Apellido`, `Fnacimiento`, `Posición`, `NCamiseta`, `titular`) 
# VALUES (NULL, 'foto ', 'jhon', 'aya ', '2022-06-03', 'delantero', '5', 'si');


# INSERT INTO `base_equipo` (`id`, `Nombre_Equipo`, `Imagen`, `Escudo`) 
# VALUES (NULL, 'sdf', 'sdf', 'sdf');

# (Null,'Qatar','https://bit.ly/3GVbHlF','https://bit.ly/3tgAv1P'),
# (Null,'Alemania','https://bit.ly/3NJz83E','https://bit.ly/3tgAv1P'),
# (Null,'Dinamarca','https://bit.ly/3PZpWtT','https://bit.ly/3tgAv1P'),
# (Null,'Brasil','https://bit.ly/3tel0aT','https://bit.ly/3tgAv1P'),
# (Null,'Francia','https://bit.ly/3NkmR5I','https://bit.ly/3tgAv1P'),
# (Null,'Bélgica','https://bit.ly/3tiuWjt','https://bit.ly/3tgAv1P'),
# (Null,'Croacia','https://bit.ly/3zosCv0','https://bit.ly/3tgAv1P'),
# (Null,'España','https://bit.ly/3aGHw5J','https://bit.ly/3tgAv1P'),
# (Null,'Serbia','https://bit.ly/3mbgWEn','https://bit.ly/3tgAv1P'),
# (Null,'Inglaterra','https://bit.ly/3NW7tN5','https://bit.ly/3tgAv1P'),
# (Null,'Suiza','https://bit.ly/3mb4Rio','https://bit.ly/3tgAv1P'),
# (Null,'Holanda','https://bit.ly/3Mijefe','https://bit.ly/3tgAv1P'),
# (Null,'Argentina','https://bit.ly/38Nb3tZ','https://bit.ly/3tgAv1P'),
# (Null,'Irán','https://bit.ly/3wZpAKU','https://bit.ly/3tgAv1P'),
# (Null,'Corea del Sur','https://bit.ly/3MfoWi7','https://bit.ly/3tgAv1P'),
# (Null,'Japón','https://bit.ly/3GNK264','https://bit.ly/3tgAv1P'),
# (Null,'Arabia Saudí','https://bit.ly/3aoLKP6','https://bit.ly/3tgAv1P'),
# (Null,'Ecuador','https://bit.ly/3te6xeK','https://bit.ly/3tgAv1P'),
# (Null,'Uruguay','https://bit.ly/3zcmc2d','https://bit.ly/3tgAv1P'),
# (Null,'Canadá','https://bit.ly/3NUD6qk','https://bit.ly/3tgAv1P'),
# (Null,'Estados Unidos','https://bit.ly/3NTDg0Z','https://bit.ly/3tgAv1P'),
# (Null,'México','https://bit.ly/3miWLnK','https://bit.ly/3x71ttZ'),
# (Null,'Ghana','https://bit.ly/392OXUu','https://bit.ly/3tgAv1P'),
# (Null,'Senegal','https://bit.ly/3xanrwl','https://bit.ly/3tgAv1P'),
# (Null,'Polonia','https://bit.ly/3tfq12Q','https://bit.ly/3tgAv1P'),
# (Null,'Portugal','https://bit.ly/3GORbmz','https://bit.ly/3tgAv1P'),
# (Null,'Túnez','https://bit.ly/3NjSWLa','https://bit.ly/3tgAv1P'),
# (Null,'Marruecos','https://bit.ly/3xfiPWM','https://bit.ly/3tgAv1P'),
# (Null,'Camerú','https://bit.ly/3GRQKrY','https://bit.ly/3tgAv1P');

