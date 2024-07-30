import QtGraphicalEffects 1.0
import QtQuick 2.11
import QtQuick.Controls 2.4

Item {
    id: sessionButton

    // define properties
    property var selectedSession: selectSession.currentIndex
    property string textConstantSession
    property Control exposeSession: selectSession

    // layout
    height: 50
    width: 150

    ComboBox {
        id: selectSession

        //model
        model: sessionModel
        currentIndex: model.lastIndex
        textRole: "name"
        hoverEnabled: true
        Keys.onPressed: {
            if (event.key == Qt.Key_Up && !popup.opened)
                currentIndex = currentIndex + 1;

            if (event.key == Qt.Key_Up && !popup.opened)
                currentIndex = currentIndex + 1;

            if (event.key == Qt.Key_Down && !popup.opened)
                systemButtons.children[0].focus = true, systemButtons.children[0].state = "focused", currentIndex = currentIndex - 1;

            if ((event.key == Qt.Key_Left || event.key == Qt.Key_Right) && !popup.opened)
                popup.open();

        }
        //define states
        states: [
            State {
                name: "pressed"
                when: selectSession.down

                PropertyChanges {
                    target: displayedItem
                    color: Qt.darker(root.palette.highlight, .1)
                }

                PropertyChanges {
                    target: selectSession.background
                    border.color: Qt.darker(root.palette.highlight, 1.1)
                }

            },
            State {
                name: "hovered"
                when: selectSession.hovered

                PropertyChanges {
                    target: displayedItem
                    color: Qt.lighter(root.palette.highlight, 1.1)
                }

                PropertyChanges {
                    target: selectSession.background
                    border.color: Qt.lighter(root.palette.highlight, 1.1)
                }

            },
            State {
                name: "focused"
                when: selectSession.visualFocus

                PropertyChanges {
                    target: displayedItem
                    color: root.palette.highlight
                }

                PropertyChanges {
                    target: selectSession.background
                    border.color: root.palette.highlight
                }

            }
        ]
        transitions: [
            Transition {
                PropertyAnimation {
                    properties: "color, border.color"
                    duration: 150
                }

            }
        ]

        // diable indicator
        indicator {
            visible: false
        }

        //delegate
        delegate: ItemDelegate {
            id: delegate

            width: parent.width
            anchors.horizontalCenter: parent.horizontalCenter
            highlighted: parent.highlightedIndex === index

            contentItem: Text {
                text: model.name
                font.pointSize: root.font.pointSize * 0.9
                color: selectSession.highlightedIndex === index ? root.palette.highlight.hslLightness >= 0.7 ? "#16161E" : "white" : root.palette.window.hslLightness >= 0.8 ? root.palette.highlight.hslLightness >= 0.8 ? "#16161E" : root.palette.highlight : "white"
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                anchors.bottomMargin: 10
            }

            background: Rectangle {
                radius: config.CornerRadius
                color: selectSession.highlightedIndex === index ? root.palette.highlight : Qt.rgba(2 / 255, 13 / 255, 24 / 255, 0.6)
                border.color: Qt.rgba(2 / 255, 13 / 255, 24 / 255, 0.4)
            }

        }

        contentItem: Text {
            id: displayedItem

            padding: 5
            text: selectSession.currentText
            verticalAlignment: Text.AlignVCenter
            anchors.left: parent.left
            anchors.leftMargin: 3
            font.pointSize: root.font.pointSize * 0.9
            Keys.onReleased: parent.popup.open()
            color: selectSession.pressed ? config.EngineeringOrange : root.palette.text
        }

        background: Rectangle {
            border.width: selectedSession.visualFocus ? 0.5 : 0
            border.color: config.EngineeringOrange
            color: Qt.rgba(2 / 255, 13 / 255, 24 / 255, 0.4)
            width: displayedItem.implicitWidth
            anchors.leftMargin: 3
            height: selectSession.visualFocus ? 2 : 0
        }

        popup: Popup {
            id: popupHandler

            y: parent.height - 1
            x: config.ForceRightToLeft == "true" ? -loginButtonWidth + displayedItem.width : 0
            width: sessionButton.width
            implicitHeight: contentItem.implicitHeight
            padding: 10

            contentItem: ListView {
                clip: true
                implicitHeight: contentHeight + 20
                model: selectSession.popup.visible ? selectSession.delegateModel : null
                currentIndex: selectSession.highlightedIndex

                ScrollIndicator.vertical: ScrollIndicator {
                }

            }

            background: Rectangle {
                radius: config.CornerRadius
                color: config.EngineeringOrange
                layer.enabled: true

                layer.effect: DropShadow {
                    transparentBorder: true
                    horizontalOffset: 0
                    verticalOffset: 0
                    radius: 30 * config.InterfaceShadowSize
                    samples: 41 * config.InterfaceShadowSize
                    cached: true
                    color: Qt.hsla(255, 125, 1, config.InterfaceShadowOpacity)
                }

            }

            enter: Transition {
                NumberAnimation {
                    property: "opacity"
                    from: 0
                    to: 1
                }

            }

        }

    }

}
