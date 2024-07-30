// TextField {
//     id: inputField
//     focus: true
//     selectByMouse: true
//     renderType: Text.NativeRendering
//     font.family: fontFamily
//     font.pointSize: fontSize
//     font.bold: true
//     horizontalAlignment: TextInput.AlignHCenter
//     background: Rectangle {
//         id: fieldBackground
//         border.color: config.EngineeringOrange
//         radius: config.CornerRadius
//         color: config.DutchWhite
//     }
// }

import QtGraphicalEffects 1.0
import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11

Column {
    id: inputContainer

    property Control exposeSession: sessionSelect.exposeSession

    Layout.fillWidth: true

    Item {
        id: usernameField

        anchors.horizontalCenter: parent.horizontalCenter

        ComboBox {
            id: selectUser

            property var popkey: config.ForceRightToLeft == "true" ? Qt.Key_Right : QtKey_Left

            width: parent.width
            height: parent.height
            anchors.left: parent.left
            Keys.onPressed: {
                if (event.key == Qt.Key_Down && !popup.opened)
                    username.forceActiveFocus();

                if ((event.key == Qt.Key_Up || event.key == popkey) && !popup.opened)
                    popup.open();

            }
            KeyNavigation.down: username
            KeyNavigation.right: username
            z: 2
            model: userModel
            currentIndex: model.lastIndex
            textRole: "name"
            hoverEnabled: true
            onActivated: {
                username.text = currentText;
            }
            states: [
                State {
                    name: "pressed"
                    when: selectUser.down

                    PropertyChanges {
                        target: usernameIcon
                        icon.color: Qt.lighter(root.palette.highlight, 1.1)
                    }

                },
                State {
                    name: "hovered"
                    when: selectUser.hovered

                    PropertyChanges {
                        target: usernameIcon
                        icon.color: Qt.lighter(root.palette.highlight, 1.2)
                    }

                },
                State {
                    name: "focused"
                    when: selectUser.activeFocus

                    PropertyChanges {
                        target: usernameIcon
                        icon.color: root.palette.highlight
                    }

                }
            ]
            transitions: [
                Transition {
                    PropertyAnimation {
                        properties: "color, border.color, icon.color"
                        duration: 150
                    }

                }
            ]

            delegate: ItemDelegate {
                width: parent.width
                anchors.horizontalCenter: parent.horizontalCenter
                highlighted: parent.highlightedIndex === index

                contentItem: Text {
                    text: model.name
                    font.pointSize: root.font.pointSize * 0.8
                    font.capitalization: Font.Capitalize
                    color: selectUser.highlightedIndex === index ? root.palette.highlight.hslLightness >= 0.7 ? "#16161E" : "white" : root.palette.window.hslLightness >= 0.8 ? root.palette.highlight.hslLightness >= 0.8 ? "#16161E" : root.palette.highlight : "white"
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                }

                background: Rectangle {
                    color: selectUser.highlightedIndex === index ? root.palette.highlight : "transparent"
                }

            }

            indicator: Button {
                id: usernameIcon

                width: selectUser.height * 0.8
                height: parent.height
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                anchors.leftMargin: selectUser.height * 0.125
                icon.height: parent.height * 0.25
                icon.width: parent.height * 0.25
                enabled: false
                icon.color: root.palette.text
                icon.source: Qt.resolvedUrl("assets/user.svg")
            }

            background: Rectangle {
                color: "transparent"
                border.color: "transparent"
            }

            popup: Popup {
                y: parent.height - username.height / 3
                x: config.ForceRightToLeft == "true" ? -loginButton.width + selectUser.width : 0
                rightMargin: config.ForceRightToLeft == "true" ? root.padding + usernameField.width / 2 : undefined
                width: usernameField.width
                implicitHeight: contentItem.implicitHeight
                padding: 10

                contentItem: ListView {
                    clip: true
                    implicitHeight: contentHeight + 20
                    model: selectUser.popup.visible ? selectUser.delegateModel : null
                    currentIndex: selectUser.highlightedIndex

                    ScrollIndicator.vertical: ScrollIndicator {
                    }

                }

                background: Rectangle {
                    radius: config.RoundCorners / 2
                    color: root.palette.window
                    layer.enabled: true

                    layer.effect: DropShadow {
                        transparentBorder: true
                        horizontalOffset: 0
                        verticalOffset: 10 * config.InterfaceShadowSize
                        radius: 20 * config.InterfaceShadowSize
                        samples: 41 * config.InterfaceShadowSize
                        cached: true
                        color: Qt.hsla(0, 0, 0, config.InterfaceShadowOpacity)
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

        TextField {
            id: username

            text: config.ForceLastUser == "true" ? selectUser.currentText : null
            font.capitalization: config.AllowBadUsernames == "false" ? Font.Capitalize : Font.MixedCase
            anchors.centerIn: parent
            height: root.font.pointSize * 3
            width: parent.width
            placeholderText: config.TranslatePlaceholderUsername || textConstants.userName
            selectByMouse: true
            horizontalAlignment: TextInput.AlignHCenter
            renderType: Text.QtRendering
            onFocusChanged: {
                if (focus)
                    selectAll();

            }
            onAccepted: loginButton.clicked()
            KeyNavigation.down: password
            z: 1
            states: [
                State {
                    name: "focused"
                    when: username.activeFocus

                    PropertyChanges {
                        target: username.background
                        border.color: root.palette.highlight
                    }

                    PropertyChanges {
                        target: username
                        color: root.palette.highlight
                    }

                }
            ]

            background: Rectangle {
                color: "transparent"
                border.color: root.palette.text
                border.width: parent.activeFocus ? 2 : 1
                radius: config.RoundCorners || 0
            }

        }

    }

    Item {
        id: passwordField

        height: root.font.pointSize * 4.5
        width: parent.width / 2
        anchors.horizontalCenter: parent.horizontalCenter
        states: [
            State {
                name: "focused"
                when: password.activeFocus

                PropertyChanges {
                    target: password.background
                    border.color: root.palette.highlight
                }

                PropertyChanges {
                    target: password
                    color: root.palette.highlight
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

        TextField {
            id: password

            anchors.centerIn: parent
            height: root.font.pointSize * 3
            width: parent.width
            focus: config.ForcePasswordFocus == "true" ? true : false
            selectByMouse: true
            echoMode: revealSecret.checked ? TextInput.Normal : TextInput.Password
            placeholderText: config.TranslatePlaceholderPassword || textConstants.password
            horizontalAlignment: TextInput.AlignHCenter
            passwordCharacter: "•"
            passwordMaskDelay: config.ForceHideCompletePassword == "true" ? undefined : 1000
            renderType: Text.QtRendering
            onAccepted: loginButton.clicked()
            KeyNavigation.down: revealSecret

            background: Rectangle {
                color: "transparent"
                border.color: root.palette.text
                border.width: parent.activeFocus ? 2 : 1
                radius: config.RoundCorners || 0
            }

        }

    }

    Item {
        height: root.font.pointSize * 2.3
        width: parent.width / 2
        anchors.horizontalCenter: parent.horizontalCenter

        Label {
            id: errorMessage

            width: parent.width
            text: failed ? config.TranslateLoginFailedWarning || textConstants.loginFailed + "!" : keyboard.capsLock ? config.TranslateCapslockWarning || textConstants.capslockWarning : null
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: root.font.pointSize * 0.8
            font.italic: true
            color: root.palette.text
            opacity: 0
            states: [
                State {
                    name: "fail"
                    when: failed

                    PropertyChanges {
                        target: errorMessage
                        opacity: 1
                    }

                },
                State {
                    name: "capslock"
                    when: keyboard.capsLock

                    PropertyChanges {
                        target: errorMessage
                        opacity: 1
                    }

                }
            ]
            transitions: [
                Transition {
                    PropertyAnimation {
                        properties: "opacity"
                        duration: 100
                    }

                }
            ]
        }

    }

    Connections {
        target: sddm
        onLoginSucceeded: {
        }
        onLoginFailed: {
            failed = true;
            resetError.running ? resetError.stop() && resetError.start() : resetError.start();
        }
    }

    Timer {
        id: resetError

        interval: 2000
        onTriggered: failed = false
        running: false
    }

}
