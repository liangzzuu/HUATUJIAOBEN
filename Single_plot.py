#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================#
import matplotlib.pyplot as plt
from matplotlib import ticker
#==============================================================================#
#%%
def Set_single_plot(dpi, figsize, seteq):
    #A4 size(11.693, 8.268)
    if figsize == 'land':
        size = [11.693, 8.268]
    elif figsize == 'port':
        size = [8.268, 11.693]
    fig = plt.figure(constrained_layout=False, dpi=dpi,
                     figsize=(size[0], size[1]))
    plt.rcParams['text.usetex'] = False
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.labelsize'] = 25
    plt.rcParams['ytick.labelsize'] = 25
    ax = fig.add_subplot(111)
    #Border
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.spines['top'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)
    #
    ax.tick_params(axis='both', which='both', bottom=True, top=True, length = 16,
                   left=True, right=True, labelleft=True, labelbottom=True,
                   labelsize=40, direction='in', pad = 15, width = 3)
    ax.tick_params(axis='both', which='minor', bottom=True, top=True, length = 9,
                   left=True, right=True, labelleft=True, labelbottom=True,
                   labelsize=40, direction='in', pad = 15, width = 3)
    #
    if seteq=='equal':
        ax.set_aspect('equal')
    #
    #增加横纵坐标label
    ax.set_xlabel(r'$X$ [cm]', fontsize = 40, labelpad = 10)
    ax.set_ylabel(r'$Y$ [cm]', fontsize = 40, labelpad = 10)      
    
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-1.25, 1.75)
    ax.minorticks_on()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    
    # ax.text(1.01, 1.07, 'MeV',
    #         fontsize = 25, ha = 'left',
    #         va = 'center', color = 'black', bbox = dict(facecolor = 'none',
    #         edgecolor = 'none', boxstyle = 'square,pad=0.3', linewidth=2),
    #         font = 'Times New Roman',transform=ax.transAxes)
    
    # ax.legend(loc='upper right', bbox_to_anchor=(0.65, 0.95),#bbox_to_anchor=(0.5, 0.8),
    #           markerscale=1.0, ncol=2, edgecolor='none',
    #           frameon=True, framealpha=1,fancybox=False, shadow=True,
    #           prop={'family': 'Times New Roman', 'size': 30})
    
    #
    # plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.20)
    # fig_name=f'N{N}_Z{Z}_opt_parmas_{NUC2[INUC]}.pdf'
    # plt.savefig(f'figure/{fig_name}',format='pdf')
    # plt.show()
    # plt.close()
    #
    return fig, ax
#==============================================================================#
#%%
fig,ax = Set_single_plot(100,'land','equal')

ax.plot([1,1,0,-1,-1,-1,0,1,1],[0,1,1,1,0,-1,-1,-1,0],
        c='r',lw=3,label='Red square')
ax.plot([1,0,-1,0,1],[0,1,0,-1,0],
        c='b',lw=3,label='Blue square')

ax.legend(loc='upper right', bbox_to_anchor=(0.95, 0.96),
          markerscale=1.0, ncol=2, edgecolor='none',
          frameon=True, framealpha=1,fancybox=False, shadow=True,
          prop={'family': 'Times New Roman', 'size': 30})

plt.show()
