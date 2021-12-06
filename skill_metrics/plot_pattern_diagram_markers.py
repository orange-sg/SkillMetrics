import matplotlib.pyplot as plt
import matplotlib.colors as clr
import matplotlib
import warnings
from skill_metrics import add_legend

def plot_pattern_diagram_markers(X,Y,option):
    '''
    Plots color markers on a pattern diagram.
    
    Plots color markers on a target diagram according their (X,Y) 
    locations. The symbols and colors are chosen automatically with a 
    limit of 70 symbol & color combinations.
    
    The color bar is titled using the content of option['titleColorBar'] 
    (if non-empty string).
    
    INPUTS:
    x : x-coordinates of markers
    y : y-coordinates of markers
    z : z-coordinates of markers (used for color shading)
    option : dictionary containing option values. (Refer to 
        GET_TARGET_DIAGRAM_OPTIONS function for more information.)
    option['axismax'] : maximum for the X & Y values. Used to limit
        maximum distance from origin to display markers
    option['markerlabel'] : labels for markers
    
    OUTPUTS:
    None

    Created on Nov 30, 2016
    Revised on Jan 6, 2019
    
    Author: Peter A. Rochford
        Symplectic, LLC
        www.thesymplectic.com
        prochford@thesymplectic.com
    '''

    # Set face color transparency
    alpha = option['alpha']
    
    # Set font and marker size
    fontSize = matplotlib.rcParams.get('font.size') - 2
    markerSize = option['markersize']
    
    if option['markerlegend'] == 'on':
        # Check that marker labels have been provided
        if option['markerlabel'] == '':
            raise ValueError('No marker labels provided.')

        # Plot markers of different color and shapes with labels 
        # displayed in a legend
        
        # Define markers
        # kind = ['+','o','x','s','d','^','v','p','h','*']
        # colorm = ['#c241415','#e5664b','#f58328','#f5ae4b','#ccd9f7','#74aed4','#3371b0','#194b90']
        kind = option['markersymbol']
        colorm = option['markercolor']
        if len(X) > 70:
            _disp('You must introduce new markers to plot more than 70 cases.')
            _disp('The ''marker'' character array need to be extended inside the code.')
        
        if len(X) <= len(kind):
            # Define markers with specified color
            marker = []
            markercolor = []
            if len(colorm) == len(kind):
                for i in range(len(colorm)):
                    marker.append(kind[i])
                    rgba = colorm[i] + (alpha,)
                    markercolor.append(rgba)
            else:
                print('The num of colors and markers should be equal!')
        else:
            # Define markers and colors using predefined list
            marker = []
            markercolor = [] #Bug Fix: missing array initialization
            if len(colorm) == len(kind):
                for i in range(len(colorm)):
                    marker.append(kind[i])
                    rgba = colorm[i] + (alpha,)
                    markercolor.append(rgba)
        
        # Plot markers at data points
        limit = option['axismax']
        hp = ()
        markerlabel = []
        for i, xval in enumerate(X):
            if abs(X[i]) <= limit and abs(Y[i]) <= limit:
                h = plt.plot(X[i],Y[i],marker[i], color = markercolor[i],markersize = markerSize,
                     markerfacecolor = markercolor[i],
                     markeredgecolor = markercolor[i],
                     markeredgewidth = 2)
                hp += tuple(h)
                markerlabel.append(option['markerlabel'][i])

        # Add legend
        if len(markerlabel) == 0:
            warnings.warn('No markers within axis limit ranges.')
        else:
            add_legend(markerlabel, option, markercolor, markerSize, fontSize, hp)
    else:
        # Plot markers as dots of a single color with accompanying labels
        # and no legend
        
        # Plot markers at data points
        limit = option['axismax']
        rgba = option['markercolor'] + (alpha,)
        for i,xval in enumerate(X):
            if abs(X[i]) <= limit and abs(Y[i]) <= limit:
                # Plot marker
                marker = option['markersymbol']
                plt.plot(X[i],Y[i],marker[i], color = rgba[i],markersize = markerSize,
                     markerfacecolor = rgba[i],
                     markeredgecolor = rgba[i])
                
                # Check if marker labels provided
                if type(option['markerlabel']) is list:
                    # Label marker
                    xtextpos = X[i]
                    ytextpos = Y[i]
                    plt.text(xtextpos,ytextpos,option['markerlabel'][i], 
                             color = option['markerlabelcolor'],
                             verticalalignment = 'bottom',
                             horizontalalignment = 'right',
                             fontsize = fontSize)

        # Add legend if labels provided as dictionary
        markerlabel = option['markerlabel']
        if type(markerlabel) is dict:
            add_legend(markerlabel, option, rgba, markerSize, fontSize)

def _disp(text):
    print(text)
