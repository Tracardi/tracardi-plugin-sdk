from tracardi_plugin_sdk.domain.register import Spec, Form

schema = {
    "form": {
        "title": "Form title",
        "groups": [
            {
                "name": "Grupa",
                "description": "Group description",
                "fields": []
            },
            {
                "name": "Grupa",
                "description": "Group description",
                "fields": [
                    {
                        "id": "id1",
                        "component": {
                            "type": "text",
                            "props": {
                                "label": "source",
                                "style": {
                                    "margin": 10
                                },
                                "required": True,

                            }
                        },
                        "name": "Copy traits to",
                        "description": "Field description",
                        "validation": {
                            "regex": "^[a-zA-Z0–9 ]+$",
                            "message": "Only contain alphanumeric characters allowed"
                        }

                    },
                    {
                        "id": "id2",
                        "component": {
                            "type": "textarea",
                            "props": {
                                "label": "test",
                                "style": {
                                    "margin": 10
                                },
                                "required": True,
                                "value": "xxx"
                            }
                        },
                        "name": "Copy traits to",
                        "description": "Field description",
                        "validation": {
                            "regex": "^[a-zA-Z0–9 ]+$",
                            "message": "Only contain alphanumeric characters allowed"
                        }
                    },
                    {
                        "id": "id3",
                        "component": {
                            "type": "resources",
                            "props": {
                                "required": True,
                            }
                        },
                        "name": "Copy traits from",
                        "description": "Field description",
                        "validation": {
                            "regex": "^[a-zA-Z0–9 ]+$",
                            "message": "Only contain alphanumeric characters allowed"
                        }

                    }
                ]
            }
        ]
    }
}


x = Form(**schema['form'])
