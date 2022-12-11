import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Controls.Material.impl 2.12

Pane {
    property var n_color
    id: control
    property int radius: 10
    background: Rectangle {
        color: n_color
        radius: control.Material.elevation > 0 ? control.radius : 0

        layer.enabled: control.enabled && control.Material.elevation > 0
        layer.effect: Elevation {
            elevation: control.Material.elevation
        }
    }
}