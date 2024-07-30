import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

RowLayout {
    Item {
        implicitHeight: powerButton.height
        implicitWidth: powerButton.width

        Button {
            id: powerButton

            height: inputHeight
            width: inputHeight
            hoverEnabled: true
            onClicked: sddm.powerOff()
            states: [
                State {
                    name: "hovered"
                    when: powerButton.hovered

                    PropertyChanges {
                        target: powerButtonBackground
                        color: config.rosewater
                    }

                }
            ]

            icon {
                source: Qt.resolvedUrl("../assets/shutdown.svg")
                height: height
                width: width
                color: config.crust
            }

            background: Rectangle {
                id: powerButtonBackground

                radius: 3
                color: config.red
            }

            transitions: Transition {
                PropertyAnimation {
                    properties: "color"
                    duration: 300
                }

            }

        }

    }

    Item {
        implicitHeight: rebootButton.height
        implicitWidth: rebootButton.width

        Button {
            id: rebootButton

            height: inputHeight
            width: inputHeight
            hoverEnabled: true
            onClicked: sddm.reboot()
            states: [
                State {
                    name: "hovered"
                    when: rebootButton.hovered

                    PropertyChanges {
                        target: rebootButtonBackground
                        color: config.rosewater
                    }

                }
            ]

            icon {
                source: Qt.resolvedUrl("../assets/reboot.svg")
                height: height
                width: width
                color: config.crust
            }

            background: Rectangle {
                id: rebootButtonBackground

                radius: 3
                color: config.red
            }

            transitions: Transition {
                PropertyAnimation {
                    properties: "color"
                    duration: 300
                }

            }

        }

    }

    Item {
        implicitHeight: sleepButton.height
        implicitWidth: sleepButton.width

        Button {
            id: sleepButton

            height: inputHeight
            width: inputHeight
            hoverEnabled: true
            onClicked: sddm.suspend()
            states: [
                State {
                    name: "hovered"
                    when: sleepButton.hovered

                    PropertyChanges {
                        target: sleepButtonBg
                        color: config.rosewater
                    }

                }
            ]

            icon {
                source: Qt.resolvedUrl("../assets/sleep.svg")
                height: height
                width: width
                color: config.crust
            }

            background: Rectangle {
                id: sleepButtonBg

                color: config.red
                radius: 3
            }

            transitions: Transition {
                PropertyAnimation {
                    properties: "color"
                    duration: 300
                }

            }

        }

    }

}
