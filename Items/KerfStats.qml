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
    property var average_value: "null"
    property var amplitude_value: "null"
    property var max_value: "null"
    property var min_value: "null"
    property var correlation_value: "null"
    property var plot_color
    height: layout.height+20
    width: layout.width
    Rectangle {
            anchors.top: layout.top
            anchors.right: layout.left
            anchors.rightMargin: 20
            width: 8
            height: layout.height
            color: plot_color
    }
    ColumnLayout{
        id: layout
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.horizontalCenterOffset: 20
        Label{
            id: average
            visible: average_value != "null"
            text: "average: "+ average_value
            Layout.preferredHeight: 20
            font.family:"roboto"
            font.pointSize: 12
        }
        Label{
            id: amplitude
            visible: amplitude_value != "null"
            text: "amplitude: "+ amplitude_value
            Layout.preferredHeight: 20
            font.family:"roboto"
            font.pointSize: 12
        }
        Label{
            id: max
            visible: max_value != "null"
            text: "max: "+ max_value
            Layout.preferredHeight: 20
            font.family:"roboto"
            font.pointSize: 12
        }
        Label{
            id: min
            visible: min_value != "null"
            text: "min: "+ min_value
            Layout.preferredHeight: 20
            font.family:"roboto"
            font.pointSize: 12
        }
        Label{
            id: corellation
            visible: correlation_value != "null"
            text: "correlation: "+ correlation_value
            Layout.preferredHeight: 20
            font.family:"roboto"
            font.pointSize: 12
        }
    }
}