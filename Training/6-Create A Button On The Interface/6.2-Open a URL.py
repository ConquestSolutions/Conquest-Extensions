##########
#
# STEP 6.2: THIS SCRIPT CREATES A HYPERLINK WHICH OPENS IN ANOTHER BROWSER WINDOW
# Copy this code into ActionLoadInterfaceContent.
#
#NOTE: To test this, you'll need to save the script and then open up an request. There you'll see a button.
#      Add some address values and watch it assign a location field.
#
##########

from System import *
from System.Windows import *
from System.Windows.Controls import *
from Conquest import *

#add the location to a google maps query
googleMapsButton = HyperlinkButton()
googleMapsButton.NavigateUri = Uri("http://maps.google.com/maps?z=12&t=m&q=" + str(source.Location))
googleMapsButton.TargetName = "_blank"
googleMapsButton.Content = "View in GIS"

panel = StackPanel()
panel.Children.Add(googleMapsButton)
panel.Margin = Thickness(2,2,2,2)

source.InterfaceContent = panel