import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Controls.Material.impl 2.12

import Backend 1.0
import CustomStyle 1.0
import "Items"

ApplicationWindow {
    id: applicationWindow
    flags: Qt.Window
    visible: true
    width: 1200
    height: 800
    visibility: Window.Maximized
    title: qsTr("template")
    property var number_of_menus: 3
    CustomStyle {
        id: customStyle
    }
    Material.theme: Material.Dark
    Pane {
        id: main_background
        padding: 0
        anchors.fill: parent
        background: Rectangle {
                anchors.fill: parent
                color: customStyle.color_background
            }
        Pane { 
            id: left_menu
            z: 2
            width: 64
            padding: 0
            height: parent.height
            anchors.top: applicationWindow.top
            anchors.left: parent.left
            background: Rectangle {
                anchors.fill: parent
                color: customStyle.color_left_menu
            }
            ColumnLayout{
                id: icons
                anchors.top: parent.top
                anchors.left: parent.left
                anchors.right: parent.right
                spacing: 1
                Item{
                    id: logo
                    Layout.preferredWidth: parent.width
                    Layout.preferredHeight: parent.width
                    Image{
                        anchors.centerIn: parent
                        source: "img/logo.png"
                    }
                }
                KerfIcon{
                    image_name: "map"
                }
                KerfIcon{
                    image_name: "pollution"
                }
                KerfIcon{
                    image_name: "weather"
                }
            }
        }
        Pane{ 
                id: side_menu
                z:1
                property var max_width: 300
                width: 0
                height: left_menu.height
                anchors.top: applicationWindow.top
                anchors.left: left_menu.right
                background: Rectangle {
                        anchors.fill: parent
                        color: customStyle.color_side_menu
                }
                KerfMenu{
                    id: map
                    Image{
                        id: map_image
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.top: parent.top
                        source: "img/map.png"
                        width: parent.width
                        height: parent.width * 1.428

                    }
                    MapButton {
                        x: 89
                        y: 66
                        index: 1
                        name: "PmGdyPorebsk"
                    }
                    MapButton {
                        x: 67
                        y: 156
                        index: 2
                        name: "PmGdySzafran"
                    }
                    MapButton {
                        x: 128
                        y: 186
                        index: 3
                        name: "PmSopBiPlowc"
                    }
                    MapButton {
                        x: 188
                        y: 218
                        index: 4
                        name: "PmGdaWyzwole"
                    }
                    MapButton {
                        x: 166
                        y: 240
                        index: 5
                        name: "PmGdaLeczkow"
                    }
                    MapButton {
                        x: 179
                        y: 269
                        index: 6
                        name: "PmGdaPowWars"
                    }

                    ComboBox {
                        id: graph_type_combo
                        width: parent.width
                        anchors.top: map_image.bottom
                        anchors.horizontalCenter: parent.horizontalCenter
                        model: ListModel {
                            id: graph_type_model
                            ListElement { text: "Jedna stacja, wiele danych" }
                            ListElement { text: "Wiele stacji, jedna dana" }
                            ListElement { text: "Wiele stacji, wiele danych" }
                        }
                        onCurrentIndexChanged: {
                            update_merge_type_combo(graph_type_model.get(currentIndex).text)
                            callback.update_graph()
                        }
                    }
                    ComboBox {
                        id: merge_type_combo
                        visible: false
                        width: parent.width
                        anchors.top: graph_type_combo.bottom
                        anchors.horizontalCenter: parent.horizontalCenter
                        model: ListModel {
                            ListElement { text: "Średnia" }
                            ListElement { text: "Najwyższa wartość" }
                            ListElement { text: "Najniższa wartość" }
                        }
                        onCurrentIndexChanged: {
                            callback.update_graph()
                        }
                    }
                }
                KerfMenu{
                    id: pollution
                    ComboBox {
                        id: combo
                        visible: false
                        height: 0
                        width: parent.width
                        anchors.top: parent.top
                        anchors.horizontalCenter: parent.horizontalCenter
                        model: ListModel {
                            id: model
                            ListElement { text: "PmGdyPorebsk" }
                            ListElement { text: "PmGdySzafran" }
                            ListElement { text: "PmSopBiPlowc" }
                            ListElement { text: "PmGdaWyzwole" }
                            ListElement { text: "PmGdaLeczkow" }
                            ListElement { text: "PmGdaPowWars" }
                        }
                        //on changed
                        onCurrentIndexChanged: callback.change_station(get_combobox())
                    }
                    Pane{width: parent.width; height: 1; background: Rectangle{anchors.fill: parent; color: "white"}visible:false}
                    KerfSwitch {
                        id: pm10_switch
                        _text: "PM10"
                        anchors.top: previousItem(this).bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                    KerfSwitch {
                        id: co_switch
                        _text: "CO"
                        anchors.top: pm10_switch.bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                    KerfSwitch {
                        id: no2_switch
                        _text: "NO2"
                        anchors.top: co_switch.bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                    
                    
                }
                KerfMenu{
                    id: weather

                    KerfSwitch2 {
                        id: temp_switch
                        _text: "Temperatura"
                        _prop: "temperature"
                        anchors.top: previousItem(this).bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                    KerfSwitch2 {
                        id: humidity_switch
                        _text: "Wilgotność"
                        _prop: "humidity"
                        anchors.top: temp_switch.bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                    KerfSwitch2 {
                        id: wind_switch
                        _text: "Prędkość Wiatru"
                        _prop: "wind_speed"
                        anchors.top: humidity_switch.bottom
                        //anchors.horizontalCenter: parent.horizontalCenter
                    }
                }
            }
        Pane{
            id: center_graph
            padding: 0
            anchors.top: applicationWindow.top
            anchors.left: side_menu.right
            width: (applicationWindow.width - side_menu.width - left_menu.width) - log.width
            height: applicationWindow.height 

            

            RoundPane {
                id: graph_container
                n_color: "#2d2d2d"
                
                Material.elevation: 6
                FigureCanvas {
                    id: fig
                    objectName: "canvas"
                    anchors.fill: parent
                }
                width: 900
                height: 700
                anchors.centerIn: parent

                Pane {
                    anchors.right: parent.right
                    background: Rectangle {
                        anchors.fill: parent
                        color: "#3700B3"
                    }
                    padding: 0
                    Button {
                        padding: 0
                        anchors.fill: parent
                        text: "reset"
                        flat: true
                        onClicked: callback.reset_plot()
                    }
                }
            }
            background: Rectangle {
                anchors.fill: parent
                color: customStyle.color_background
            }
            RowLayout{
                anchors.top: parent.top
                anchors.bottom: graph_container.top
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 50
                KerfDatePicker{
                    z:1
                    id: date_picker_from
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    _name: "Od:"
                    _days: "1"
                    _months: "1"
                    _years: "2021" 
                    onDateChanged: {
                        update_date()
                        callback.set_timeline(this.get_date().getTime(), date_picker_to.get_date().getTime())
                    }
                    _maximum_date: new Date(2021, 11, 20)
                    _minimum_date: new Date(2021, 0, 1)
                }
                KerfDatePicker{
                    id: date_picker_to
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    _name: "Do:"
                    _days: "1"
                    _months: "1"
                    _years: "2022" 
                    onDateChanged: {
                        update_date()
                        callback.set_timeline(date_picker_from.get_date().getTime(), this.get_date().getTime())
                    }
                    _maximum_date: new Date(2022, 0, 1)
                    _minimum_date: new Date(2021, 0, 10)
                }
            }
        }
        Pane{
            id: log
            padding: 0
            anchors.top: applicationWindow.top
            anchors.left: center_graph.right
            width: (applicationWindow.width - side_menu.width - left_menu.width) / 6
            height: applicationWindow.height 
            background: Rectangle {
                anchors.fill: parent
                color: customStyle.color_side_menu
            }
            ListModel {
                id: log_model
            }
            ListView {
                id: log_list
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                width: parent.width
                height: parent.height
                anchors.verticalCenterOffset: 20
                model: log_model
                delegate: KerfStats {
                    plot_color: log_model.get(index).color
                    amplitude_value: log_model.get(index).amplitude
                    average_value: log_model.get(index).average
                    max_value: log_model.get(index).max
                    min_value: log_model.get(index).min
                    correlation_value: log_model.get(index).correlation
                }
            }
        }
    }
    function get_combobox() {
        return combo.model.get(combo.currentIndex).text;
    }
    function check_enum() {
        console.log(customStyle.RED)
    }
    function set_switch_state(key, state) {
        var k = key.toLowerCase()
        var obj = {
            "pm10" : pm10_switch,
            "co" : co_switch,
            "no2" : no2_switch
        }
        obj[k]._enabled = state
    }
    function set_switch_position(key, state) {
        var k = key.toLowerCase()
        var obj = {
            "pm10" : pm10_switch,
            "co" : co_switch,
            "no2" : no2_switch
        }
        obj[k]._position = state
        obj[k]._checked = state
    }
    function itemIndex(item) {
        if (item.parent == null)
            return -1
        var siblings = item.parent.children
        for (var i = 0; i < siblings.length; i++)
            if (siblings[i] == item)
                return i
        return -1 //will never happen
    }
    //returns null, if the item is not parented, or is the first one
    function previousItem(item) {
        if (item.parent == null)
            return null
        var index = itemIndex(item)
        return (index > 0)? item.parent.children[itemIndex(item) - 1]: null
    }
    //returns null, if item is not parented, or is the last one
    function nextItem(item) {
        if (item.parent == null)
            return null

        var index = itemIndex(item)
        var siblings = item.parent.children

        return (index < siblings.length - 1)? siblings[index + 1]: null
    }
    function deactivate_all_icons() {
        for(var i=1; i< number_of_menus + 1; i++){
            icons.children[i].deactivate()
        }
        var menus = map.parent.children
        for(var i=0; i<number_of_menus; i++){
            menus[i].hide()
        }
        side_menu.width = 0
    }
    function show_menu(icon){
        var menus = map.parent.children
        for(var i=1; i< number_of_menus + 1; i++){
            if(icons.children[i] == icon)menus[i-1].show()
        }
        side_menu.width = side_menu.max_width
    }
    function update_merge_type_combo(name){
        if(name == "Wiele stacji, wiele danych")
            merge_type_combo.visible = true
        else
            merge_type_combo.visible = false

        if(name == "Jedna stacja, wiele danych")
            deactivate_all_map_buttons()

        if(name == "Wiele stacji, jedna dana")
            set_switches_mode_one()
        else 
            set_switches_mode_many()
    }
    function deactivate_all_map_buttons(){
        for(var i=1; i<map.children.length-2; i++){
            map.children[i].deactivate()
        }
    }
    function get_map_button_checked_count(){
        var count = 0
        for(var i=0; i<map.children.length; i++){
            if(map.children[i].state == "on")
                count++
        }
        if (count > 0) return 1
        else return 0
    }
    function buttonid_to_station(id) {
        var button = id - 1
        var station = model.get(button).text
        return station
    }
    function deactivate_all_switches(exception_text){
        for(var i=2; i<pollution.children.length; i++){
            if(pollution.children[i]._text != exception_text){
                if(pollution.children[i].is_checked())
                    pollution.children[i].deactivate()
            }
        }
    }
    function deactivate_all_weather_switches(){
        for(var i=0; i<weather.children.length; i++){
            weather.children[i].deactivate()
        }
    }
    function set_switches_mode_one(){         
        for(var i=2; i<pollution.children.length; i++){
            pollution.children[i].deactivate()
            pollution.children[i].set_mode_one()
        }
    }
    function set_switches_mode_many(){ 
        for(var i=2; i<pollution.children.length; i++){
            pollution.children[i].set_mode_many()
        }
    }
    function get_mode() {
        return graph_type_combo.currentIndex
    }
    function set_button_state(station, state) {
        console.log(station, state)
        //get station index from model
        var index = 0
        for(var i=0; i<model.count; i++){
            if(model.get(i).text == station){
                index = i
                break
            }
        }
        //set button state
        map.children[index+1].state = state
    }
    function get_merge_type_combo() {
        return merge_type_combo.currentIndex
    }
    function update_date(){
        var start = new Date(date_picker_from.get_date())
        start.setDate(start.getDate() + 10)
        var end = new Date(date_picker_from.get_date())
        end.setDate(end.getDate() - 10)
        date_picker_to.set_min_date(start)
        date_picker_from.set_max_date(end)
    }
    function log_model_append(e) {
        log_model.append(e)
    }
    function log_model_clear() {
        log_model.clear()
    }
}