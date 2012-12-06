'''
Factory for GUIs.
'''

from src.gui.gui import GUI, TextGUI, GraphGUI

def get_gui(name='text', data_type='default'):
    '''Get a GUI from a string.'''
    print('Using {0}-based GUI'.format(name))
    if name == 'text':
        return TextGUI(data_type) 
    if name == 'graph':
        return GraphGUI(data_type)

    return GUI(data_type)
