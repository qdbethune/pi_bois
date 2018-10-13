import QtQuick 2.6
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.2
import QtQuick.Window 2.2

Window { /* Used to show how different types of lights work on the form
            with demo music*/
    id: demo_window
    visible: true
    width: 320
    height: 480
    color: "#a4a4a4"
    opacity: 1
    title: qsTr("Hello World")

    Button {
        id: btn_go
        x: 83
        width: 154
        height: 72
        text: qsTr("Start")
        style: ButtonStyle {
              label: Text {
                renderType: Text.NativeRendering
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 20
                text: control.text
              }
        }
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 40
    }

    Connections {
        target: btn_go
        onClicked: { // TODO: Change so it starts music and executes visualization
            print("clicked") // REPLACE HERE
        }
    }

    Rectangle {
        id: tri_left
        y: 372
        width: 50
        height: 50
        color: "#ffffff"
        anchors.verticalCenter: tri_mid.verticalCenter
        anchors.left: parent.left
        anchors.leftMargin: 40
        border.width: 1
    }

    Rectangle {
        id: tri_mid
        x: 135
        y: 372
        width: 50
        height: 50
        color: "#ffffff"
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 45
        anchors.horizontalCenter: parent.horizontalCenter
        border.width: 1
    }

    Rectangle {
        id: stereo_left
        width: 50
        height: 50
        color: "#ffffff"
        anchors.left: parent.left
        anchors.leftMargin: 85
        anchors.top: light_gradient.bottom
        anchors.topMargin: 30
        border.width: 1
    }

    Rectangle {
        id: stereo_right
        x: 170
        width: 50
        height: 50
        color: "#ffffff"
        anchors.top: light_gradient.bottom
        anchors.topMargin: 30
        anchors.right: parent.right
        anchors.rightMargin: 85
        border.width: 1
    }

    Rectangle {
        id: light_single
        x: 132
        width: 50
        height: 50
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: btn_go.bottom
        anchors.topMargin: 32
        border.width: 1
    }

    Rectangle {
        id: tri_right
        x: 223
        y: 372
        width: 50
        height: 50
        color: "#ffffff"
        anchors.right: parent.right
        anchors.rightMargin: 40
        anchors.verticalCenter: tri_mid.verticalCenter
        border.width: 1
    }

    Rectangle {
        id: light_gradient
        x: 47
        width: 220
        height: 50
        color: "#ffffff"
        anchors.top: light_single.bottom
        anchors.topMargin: 32
        anchors.horizontalCenter: parent.horizontalCenter
        border.width: 1
    }




}

/*##^## Designer {
    D{i:2;anchors_height:72;anchors_width:154;anchors_x:83;anchors_y:42}D{i:5;anchors_height:50;anchors_x:53;anchors_y:372}
D{i:9;anchors_x:93;anchors_y:298}D{i:10;anchors_y:298}D{i:11;anchors_width:50;anchors_x:132;anchors_y:156}
D{i:8;anchors_y:226}
}
 ##^##*/
