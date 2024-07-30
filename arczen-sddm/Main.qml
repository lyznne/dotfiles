/**
*   A R C  - Z E N          SDDM         THEME v.1.0
*
*   Author:  ArcZen >_ enos muthiani
*
*
*   Date:    25.07.24
*/

import QtGraphicalEffects 1.0
import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import SddmComponents 2.0
import "components"

Pane {
    id: root

    readonly property color backgroundColor: Qt.rgba(2 / 255, 13 / 255, 24 / 255, 0.4)
    readonly property color hoverBackgroundColor: Qt.rgba(2 / 255, 13 / 255, 24 / 255, 0.7)
    property int sessionIndex: session.index
    property Control exposeSession: sessionSelect.exposeSession

    height: config.ScreenHeight || Screen.height
    width: config.ScreenWidth || Screen.width
    LayoutMirroring.enabled: Qt.locale().textDirection == Qt.RightToLeft
    LayoutMirroring.childrenInherit: true
    padding: config.ScreenPadding
    palette.button: "transparent"
    palette.highlight: config.EngineeringOrange
    palette.text: config.DutchWhite
    palette.buttonText: config.DutchWhite
    palette.window: config.BackgroundColor
    font.family: config.Font
    font.pointSize: config.FontSize !== "" ? config.FontSize : parseInt(height / 80)
    focus: true

    TextConstants {
        id: textConstants
    }

    Connections {
        function onLoginSucceeded() {
            pw_entry.clear();
            pw_entry.focus = true;
            errorMsgContainer.visible = true;
        }

        function onLoginFailed() {
            password.text = "";
            errorMessage.color = "";
            errorMessage.text = textConstants.loginFailed;
        }

        function onInformationMessage() {
            errorMessage.color = "red";
            errorMessage.text = message;
        }

        target: sddm
    }

    // Background Image
    Background {
        anchors.fill: parent
        source: config.background
        fillMode: Image.PreserveAspectCrop
        onStatusChanged: {
            if (status == Image.Error && source != config.defaultBackground)
                source = config.defaultBackground;

        }
    }

    Image {
        id: backgroundImage

        anchors.fill: parent
        source: "assets/background.jpg"
        fillMode: Image.PreserveAspectCrop
        onStatusChanged: {
            if (status == Image.Error)
                source = "assets/background.jpg";

        }
    }

    Rectangle {
        id: backgroundRect

        anchors.fill: parent
        color: "transparent"

        LoginForm {
            // Background gradient
            // LinearGradient {
            //     anchors.fill: parent
            //     start: Qt.point(0, 0)
            //     end: Qt.point(0, parent.height)
            //     gradient: Gradient {
            //         GradientStop {
            //             position: 0.0296
            //             color: Qt.rgba(2 / 255, 13 / 255, 25 / 255, 0.3)
            //         }
            //         GradientStop {
            //             position: 0.9668
            //             color: Qt.rgba(10 / 255, 66 / 255, 127 / 255, 0.3)
            //         }
            //     }
            // }

            id: form

            height: virtualKeyboard.state == "visible" ? root.height - virtualKeyboard.implicitHeight : 328
            width: parent.width / 2.5
            // color: "#020D18B6"
            // border.color: Qt.rgba(1, 1, 1, 0.4)
            // radius: 3
            // opacity: 0.7
            anchors.centerIn: parent
        }

    }

    SessionButton {
        id: sessionSelect

        textConstantSession: textConstants.session
        anchors.top: parent.top
        anchors.left: parent.left
    }

    SettingButton {
        id: settingSelect

        anchors.bottom: parent.bottom
        anchors.right: parent.right 
        anchors.bottomMargin: 20 
        anchors.rightMargin: 30
    }

}
