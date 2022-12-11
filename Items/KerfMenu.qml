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
    id: kerfMenu
    property var active: false
    visible: active
    anchors.fill: parent

    function hide(){
        active = false
    }
    function show(){
        active = true
    }
}