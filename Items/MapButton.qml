import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Shapes 1.15
import QtQuick.Extras 1.4
import CustomStyle 1.0

Rectangle {
    property var index:0
    property string name: "name"
    
    border.width: 1
    border.color: customStyle.color_side_menu
    radius: 50
    id: button
    width: 16
    height: 16
    state: "off"

    ToolTip{
        id: toolTip
        contentItem: Text{
            text: button.name
            color: customStyle.color_icon
            font.pixelSize: 13
        }
        background: Rectangle {
            border.color: customStyle.color_kerf
            color: customStyle.color_background
            radius: 10
        }
    }

    states: [
        State {
            name: "off"
            PropertyChanges { target: button; color: customStyle.color_icon}
        },
        State {
            name: "on"
            PropertyChanges { target: button; color: customStyle.color_kerf }
        }
    ]

    MouseArea{
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        onHoveredChanged: {
            if(parent.state=="off"){
                parent.color = containsMouse ? customStyle.color_side_menu : customStyle.color_icon
            }
            if(parent.state=="on"){
                parent.color = containsMouse ? customStyle.color_dark_kerf : customStyle.color_kerf
            }
            toolTip.visible = parent.name ? containsMouse : false
        }
        onClicked: {
            if (graph_type_combo.currentIndex == 0 && get_map_button_checked_count() == 0 && parent.state == "off") {
                parent.state == "on" ? parent.state = "off" : parent.state = "on"
                callback.update_map_button(parent.index)
                print("change station")
                callback.change_station(buttonid_to_station(parent.index))
            }
            else if (graph_type_combo.currentIndex == 0 && get_map_button_checked_count() && parent.state == "off") {
                deactivate_all_map_buttons()
                parent.state == "on" ? parent.state = "off" : parent.state = "on"
                callback.update_map_button(parent.index)
                callback.change_station(buttonid_to_station(parent.index))
            }
            else {
                parent.state == "on" ? parent.state = "off" : parent.state = "on"
                callback.update_map_button(parent.index)
                if (parent.state == "on") {
                    callback.add_station(buttonid_to_station(parent.index))
                }
                else {
                    callback.remove_station(buttonid_to_station(parent.index))
                }
            }
        }
    }

    function deactivate() {
        if (state == "on") callback.remove_station(buttonid_to_station(index))
        state = "off"
        
    }
}