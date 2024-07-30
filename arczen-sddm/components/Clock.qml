/**
*   A R C  - Z E N          SDDM         THEME v.1.0
*
*   Author:  ArcZen >_ enos muthiani
*
*
*   Date:    25.07.24
*/

import QtQuick 2.8
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.1

ColumnLayout {
    id: clock

    spacing: 0
    Component.onCompleted: {
        dateLabel.updateTime();
        timeLabel.updateTime();
    }

    // Date
    Label {
        id: dateLabel

        function updateTime() {
            text = new Date().toLocaleDateString(Qt.locale(config.Locale), config.DateFormat == "short" ? Locale.ShortFormat : config.DateFormat !== "" ? config.DateFormat : Locale.LongFormat);
        }

        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: root.font.pointSize * 1.5
        color: root.palette.text
        renderType: Text.QtRendering
    }

    // Time
    Label {
        id: timeLabel

        function updateTime() {
            text = new Date().toLocaleTimeString(Qt.locale(config.Locale), config.HourFormat == "long" ? Locale.LongFormat : config.HourFormat !== "" ? config.HourFormat : Locale.ShortFormat);
        }

        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: root.font.pointSize * 1.1
        color: root.palette.text
        renderType: Text.QtRendering
    }

    Timer {
        interval: 1000
        repeat: true
        running: true
        onTriggered: {
            dateLabel.updateTime();
            timeLabel.updateTime();
        }
    }

}
