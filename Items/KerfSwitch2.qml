import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Shapes 1.15
import QtQuick.Extras 1.4

Item{
    id: kerfSwitch
    height: 40
    width: parent.width
    property var _text: "Kerf"
    property var _prop: ""
    property var _checked: false
    property var _position: 0
    property var _enabled: true
    property var _mode: "one"
    Label {
        text: _text
        font.pixelSize: 20
        anchors.left: parent.left
        anchors.top: parent.top
    }
    Switch {
        id: kswitch
        width: 40
        height: 40
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.horizontalCenterOffset: 5*parent.width/12
        checked: _checked
        position: _position
        enabled: _enabled
        anchors.left: previousItem(this).right
        anchors.verticalCenter: previousItem(this).verticalCenter
        onCheckedChanged: {
            if(checked){
                callback.add_weather(_prop)
            }
            else{
                callback.remove_weather(_prop)
            }
        }
        MouseArea{
        anchors.fill: parent
            onClicked:{
                if(kerfSwitch._checked) {
                    kerfSwitch._checked = false
                }
                else {
                    deactivate_all_weather_switches()
                    kerfSwitch._checked = true
                }
            }
        }
    }
    function set_mode_one(){
        _mode = "one"
    }
    function set_mode_many(){
        _mode = "many"
    }
    function deactivate(){
        if (_checked){
            callback.change_weather_setting(_prop, false)
        }
        _checked = false
    }
    function is_checked(){
        return _checked
    }
}