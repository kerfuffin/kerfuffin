import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 1.4
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Shapes 1.15
import QtQuick.Extras 1.4

Item {
    id: kerfDatePicker
    property var _days: ""
    property var _months: ""
    property var _years: ""
    property var _maximum_date: new Date(275759, 10, 25)
    property var _minimum_date: new Date(1, 1, 1)
    property var _name: "name"
    height: pickerBackground.height
    width: pickerBackground.width
    signal dateChanged()
    Pane{
        padding: 5
        id: pickerBackground
        RowLayout{
            anchors.fill: parent
            spacing: 0
            Label{
                text: _name
                font.pixelSize: 13
                Layout.rightMargin: 10
            }
            TextField {
                id: days
                property var characters: 2
                placeholderText: qsTr("dd")
                horizontalAlignment: TextInput.AlignHCenter
                text:_days
                font.bold: true
                font.family:"roboto"
                font.pointSize: 12
                Layout.minimumWidth: font.pointSize * characters
                Layout.preferredWidth: font.pointSize * (characters + 1)
                Layout.maximumWidth: font.pointSize * (characters + 2)
                MouseArea{
                    anchors.fill: parent
                }
            }
            TextField {
                id: months
                property var characters: 2
                placeholderText: qsTr("mm")
                horizontalAlignment: TextInput.AlignHCenter
                text:_months
                font.bold: true
                font.family:"roboto"
                font.pointSize: 12
                Layout.minimumWidth: font.pointSize * characters
                Layout.preferredWidth: font.pointSize * (characters + 1)
                Layout.maximumWidth: font.pointSize * (characters + 2)
                MouseArea{
                    anchors.fill: parent
                }
            }
            TextField {
                id: years
                property var characters: 4
                placeholderText: qsTr("yyyy")
                horizontalAlignment: TextInput.AlignHCenter
                text:_years
                font.bold: true
                font.family:"roboto"
                font.pointSize: 12
                Layout.minimumWidth: font.pointSize * characters
                Layout.preferredWidth: font.pointSize * (characters + 1)
                Layout.maximumWidth: font.pointSize * (characters + 2)
                MouseArea{
                    anchors.fill: parent
                }
            }
            Button {
                Layout.leftMargin: 10
                id: button
                Layout.preferredWidth: this.height
                onClicked:{
                    toggle_calendar_visibility()
                }
            }
        }
        background: Rectangle {
                anchors.fill: parent
                color: customStyle.color_side_menu
                radius: 10
        }
    }
    Calendar{
        anchors.top: pickerBackground.top
        anchors.left: pickerBackground.left
        maximumDate: parent._maximum_date
        minimumDate: parent._minimum_date
        id:cal
        visible: false
        selectedDate: new Date()
        onClicked:  {
            toggle_calendar_visibility()
            kerfDatePicker._days = Qt.formatDate(cal.selectedDate, "dd")
            kerfDatePicker._months = Qt.formatDate(cal.selectedDate, "MM")
            kerfDatePicker._years = Qt.formatDate(cal.selectedDate, "yyyy")
            kerfDatePicker.dateChanged()
        }
    }
    function toggle_calendar_visibility(){
        cal.visible ? cal.visible = false : cal.visible = true
    }
    function set_max_date(date){
        _maximum_date = date
    }
    function set_min_date(date){
        _minimum_date = date
    }
    function get_date(){
        console.log(new Date(parseInt(_years), parseInt(_months)-1, parseInt(_days)))
        return new Date(parseInt(_years), parseInt(_months)-1, parseInt(_days))
    }
}