import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
geometries = {

	'Canyon Ultimate L':{
		'reach':401,
		'reach+':490,
		'stack':583,
		'seat tube length':577,
		'seat tube height':540,
		'seat angle':73.2,
		'head angle':73.3,
		'head tube':162.1,
		'seat height':175,
		'saddle height':669,
		'wheel base':1003,
		'chainstay':413,
		'wheel size':28,
		'bb offset':73
		},
	'Canyon Ultimate M':{
		'reach':393,
		'reach+':473,
		'stack':564,
		'seat tube length':564,
		'seat tube height':510,
		'seat angle':73.1,
		'head angle':73.1,
		'head tube':142,
		'seat height':175,
		'saddle height':669,
		'wheel base':988,
		'chainstay':410,
		'wheel size':28,
		'bb offset':73
		},
	'Canyon Endurace M':{
		'reach':378,
		'reach+':453,
		'stack':590,
		'seat tube length':522,
		'seat tube height':0,
		'seat angle':73.5,
		'head angle':72.75,
		'head tube':165,
		'seat height':0,
		'saddle height':0,
		'wheel base':993,
		'chainstay':415,
		'wheel size':28,
		'bb offset':73
		},
	'Canyon Endurace L':{
		'reach':387,
		'reach+':472,
		'stack':611,
		'seat tube length':552,
		'seat tube height':0,
		'seat angle':73.5,
		'head angle':73,
		'head tube':168,
		'seat height':0,
		'saddle height':0,
		'wheel base':1006,
		'chainstay':415,
		'wheel size':28,
		'bb offset':73
		},
	'Whyte Suffolk':{
		'reach':387.3,
		'reach+':480,
		'stack':597.7,
		'seat tube length':560,
		'seat tube height':560,
		'seat angle':73.0,
		'head angle':73.0,
		'head tube':175,
		'seat height':175,
		'saddle height':0,
		'wheel base':1012.8,
		'chainstay':425,
		'wheel size':28,
		'bb offset':0
		},
	'Trek Emonda 56':{
		'reach':391,
		'reach+':391,
		'stack':563,
		'seat tube length':525,
		'seat tube height':525,
		'seat angle':73.3,
		'head angle':73.5,
		'head tube':151,
		'seat height':0,
		'saddle height':0,
		'wheel base':983,
		'chainstay':410,
		'wheel size':28,
		'bb offset':0
		},
	'Trek Emonda 58':{
		'reach':396,
		'reach+':396,
		'stack':581,
		'seat tube length':553,
		'seat tube height':553,
		'seat angle':73.0,
		'head angle':73.8,
		'head tube':171,
		'seat height':0,
		'saddle height':0,
		'wheel base':992,
		'chainstay':411,
		'wheel size':28,
		'bb offset':0
		},
	'Merida Scultura Team L':{ # recommended by size computer
		'reach':400,
		'reach+':0,
		'stack':571,
		'seat tube length':521,
		'seat tube height':521,
		'seat angle':73.0,
		'head angle':73.5,
		'head tube':155,
		'seat height':0,
		'saddle height':0,
		'wheel base':1000,
		'chainstay':408,
		'wheel size':28,
		'bb offset':66
		},
	'Trek Emonda 58':{ # recommended by size computer
		'reach':396,
		'reach+':0,
		'stack':581,
		'seat tube length':553,
		'seat tube height':553,
		'seat angle':73.0,
		'head angle':73.8,
		'head tube':171,
		'seat height':0,
		'saddle height':0,
		'wheel base':992,
		'chainstay':411,
		'wheel size':28,
		'bb offset':68
		},
	'Specialised Tarmak 58':{ # recommended by size computer
		'reach':405,
		'reach+':0,
		'stack':581,
		'seat tube length':517,
		'seat tube height':517,
		'seat angle':73.5,
		'head angle':73.5,
		'head tube':178,
		'seat height':0,
		'saddle height':0,
		'wheel base':1006,
		'chainstay':410,
		'wheel size':28,
		'bb offset':72
		},
	'Canndondalte Supersixevo 54':{ # recommended by size computer
		'reach':384,
		'reach+':0,
		'stack':555,
		'seat tube length':546,
		'seat tube height':546,
		'seat angle':73.7,
		'head angle':71.2,
		'head tube':153,
		'seat height':0,
		'saddle height':0,
		'wheel base':1010,
		'chainstay':410,
		'wheel size':28,
		'bb offset':72
		},
	'Canndondalte Supersixevo 56':{ # recommended by size computer
		'reach':390,
		'reach+':0,
		'stack':574,
		'seat tube length':536,
		'seat tube height':536,
		'seat angle':73.3,
		'head angle':730,
		'head tube':164,
		'seat height':0,
		'saddle height':0,
		'wheel base':992,
		'chainstay':408,
		'wheel size':28,
		'bb offset':72
		}
	
}
def plot_bike(p,D,color,alpha=.7):
	# stack
	p.plot([0,0]	     ,[0         ,D['stack']],ls='-',color=color,alpha=alpha)	
	# reach
	p.plot([0,D['reach']],[D['stack'],D['stack']],ls='-',color=color,alpha=alpha)	
	# reach+
	p.plot([0,D['reach+']],[D['stack'],D['stack']],ls='-',color=color,alpha=alpha)	
	th = D['seat angle']/360*2*np.pi
	p.plot([0,-np.cos(th)*D['seat tube height']],[0,np.sin(th)*D['seat tube height']],ls='-',color=color,alpha=alpha)	
	# seat tube
	p.plot([D['reach'],-np.cos(th)*D['seat tube height']],
	       [D['stack'], np.sin(th)*D['seat tube height']],ls='-',color=color,alpha=alpha)	
	# saddle height 
	p.plot([0,-np.cos(th)*D['saddle height']],[0,np.sin(th)*D['saddle height']],ls='--',color=color,alpha=alpha)	
	# head tube
	l=p.plot([D['reach'],D['reach']+np.cos(th)*D['head tube']],
	       [D['stack'],D['stack']-np.sin(th)*D['head tube']],ls='-',color=color,lw='4',alpha=alpha)	
	# chainstay
	p.axvline(-D['chainstay'],color=color,alpha=alpha)
	p.axvline(-D['chainstay']+D['wheel base'],color=color,alpha=alpha)
	if D['bb offset']!=0:
	 # wheels
	 drawObject = Circle((-D['chainstay'],D['bb offset']),radius=0.5*D['wheel size']*22.58,fill=False,color=color,alpha=alpha)
	 p.add_patch(drawObject)
	 p.plot([0,-D['chainstay']],[0,D['bb offset']],ls='--',color=color,alpha=alpha)	

	 drawObject = Circle((-D['chainstay']+D['wheel base'],D['bb offset']),radius=0.5*D['wheel size']*22.58,fill=False,color=color,alpha=alpha)
	 p.add_patch(drawObject)
	 drawObject = Circle((-D['chainstay']+D['wheel base'],D['bb offset']),radius=22.58,color=color,alpha=alpha)
	 p.add_patch(drawObject)
	 drawObject = Circle((-D['chainstay'],D['bb offset']),radius=22.58,color=color,alpha=alpha)
	 p.add_patch(drawObject)

	 # fork
	 l=p.plot([D['reach']+np.cos(th)*D['head tube'],-D['chainstay']+D['wheel base']],
	       [D['stack']-np.sin(th)*D['head tube'],D['bb offset']],ls='-',color=color,lw='2',alpha=alpha)	
	 
	
	return l


fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Canyon Ultimate M','Canyon Ultimate L','Trek Emonda 58','Specialised Tarmak 58','Merida Scultura Team L','Whyte Suffolk']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo.pdf')

fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Whyte Suffolk','Canyon Ultimate M','Canyon Ultimate L','Canyon Endurace M','Canyon Endurace L','Canndondalte Supersixevo 54']
wo = ['Whyte Suffolk','Canndondalte Supersixevo 54','Canyon Ultimate M','Canyon Ultimate L']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo2.pdf')

fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Whyte Suffolk','Canyon Endurace M','Canyon Endurace L','Canndondalte Supersixevo 54','Canndondalte Supersixevo 56']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo3.pdf')

fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Whyte Suffolk','Canyon Ultimate M','Canyon Ultimate L','Canyon Endurace M','Canyon Endurace L']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo4.pdf')

fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Whyte Suffolk','Canyon Ultimate M','Canyon Ultimate L','Canyon Endurace L','Merida Scultura Team L','Canndondalte Supersixevo 54']
wo = ['Canyon Ultimate L','Canyon Ultimate M','Canndondalte Supersixevo 54','Canndondalte Supersixevo 56']
wo = ['Whyte Suffolk','Canyon Ultimate M','Canyon Ultimate L','Canndondalte Supersixevo 54']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo5.pdf')

fig,ax	= plt.subplots(1,1,figsize=(5,5))
l=[]
wo = ['Whyte Suffolk','Canyon Ultimate M','Canyon Ultimate L','Canyon Endurace L','Merida Scultura Team L','Canndondalte Supersixevo 54']
wo = ['Canyon Ultimate L','Canndondalte Supersixevo 56']
colors = ['r','g','b','m','y','k']
sl=[]
for i,swo in enumerate(wo):
 l.append(plot_bike(ax,geometries[swo],colors[i])[0])
 sl.append(swo)
ax.legend(l,sl)
ax.set_xlim((-1000,1000))
ax.set_ylim((-300,1700))
fig.savefig('geo6.pdf')

