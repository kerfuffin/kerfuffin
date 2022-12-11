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

Item{
    id: kerfIcon
    Layout.preferredWidth: parent.width
    Layout.preferredHeight: parent.width
    property var image_type_off: "gray"
    property var image_type_on: "blue"
    property var image_name
    property var active: false
    property var image_type: image_type_off
    property var background_color: "Transparent"
    CustomStyle {
        id: customStyle
    }
    Rectangle {
        anchors.fill: parent
        color: background_color
    }
    Rectangle {
        anchors.top: parent.top
        height: parent.height
        anchors.left: parent.left
        visible: active
        width: 4
        color: customStyle.color_kerf
    }
    Image{
        source: "../img/icon_"+image_name+"_"+image_type+".png"
        anchors.centerIn: parent
    }
    MouseArea{
        anchors.fill: parent
        hoverEnabled: true
        onHoveredChanged: {
            if(!active){
                parent.image_type = containsMouse ? image_type_on : image_type_off
            }
        }
        onClicked: {
            var was_active = active
            deactivate_all_icons()
            if(!was_active){
                parent.activate()
                show_menu(parent)
            }
        }
    }
    function deactivate(){
        active = false
        background_color = "Transparent"
        image_type = image_type_off
    }
    function activate(){
        active = true
        background_color = customStyle.color_side_menu
        image_type = image_type_on
    }
}