/****************************************************************************
** Meta object code from reading C++ file 'QTColorParameterWindow.h'
**
** Created: Wed Oct 17 13:57:35 2012
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QTColorParameterWindow.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QTColorParameterWindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_CQTColorParameterWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      28,   25,   24,   24, 0x08,
      57,   24,   24,   24, 0x08,
      93,   24,   24,   24, 0x08,
     128,   24,   24,   24, 0x08,
     163,   24,   24,   24, 0x08,
     210,  203,   24,   24, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_CQTColorParameterWindow[] = {
    "CQTColorParameterWindow\0\0id\0"
    "ColorRadioButtonClicked(int)\0"
    "PrintColorParametersButtonClicked()\0"
    "LoadColorParametersButtonClicked()\0"
    "SaveColorParametersButtonClicked()\0"
    "ColorParameterFileBrowseButtonClicked()\0"
    "nValue\0SliderValueChanged(int)\0"
};

void CQTColorParameterWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        CQTColorParameterWindow *_t = static_cast<CQTColorParameterWindow *>(_o);
        switch (_id) {
        case 0: _t->ColorRadioButtonClicked((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->PrintColorParametersButtonClicked(); break;
        case 2: _t->LoadColorParametersButtonClicked(); break;
        case 3: _t->SaveColorParametersButtonClicked(); break;
        case 4: _t->ColorParameterFileBrowseButtonClicked(); break;
        case 5: _t->SliderValueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData CQTColorParameterWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject CQTColorParameterWindow::staticMetaObject = {
    { &CQTWindow::staticMetaObject, qt_meta_stringdata_CQTColorParameterWindow,
      qt_meta_data_CQTColorParameterWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &CQTColorParameterWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *CQTColorParameterWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *CQTColorParameterWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_CQTColorParameterWindow))
        return static_cast<void*>(const_cast< CQTColorParameterWindow*>(this));
    return CQTWindow::qt_metacast(_clname);
}

int CQTColorParameterWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = CQTWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
