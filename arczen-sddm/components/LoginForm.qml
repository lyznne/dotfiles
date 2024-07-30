import QtGraphicalEffects 1.0
import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import SddmComponents 2.0 as SDDM

ColumnLayout {
    // avatar

    id: formContainer

    property int p: config.ScreenPadding
    property string a: config.formPosition
    property alias systemButtonVisibility: systemButtons.visible
    property alias clockVisisbility: clock.visible
    property bool virtualKeyboardActive

    SDDM.TextConstants {
        id: textConstants
    }

    // clock
    Clock {
        id: clock

        Layout.alignment: Qt.AlignHCenter | qt.AlignBottom
        Layout.preferredHeight: root.height / 4
        Layout.leftMargin: p != "0" ? a == "left" ? -p : a == "right" ? p : 0 : 0
    }

    InputField {
        id: input

        Layout.alignment: Qt.AlignVCenter
        Layout.preferredHeight: root.height / 4
    }

    SystemButtons { 
        id: systemButtons 

        
    }

}
