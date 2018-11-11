import stream
client = stream.connect('xkwvpuatj96g', 'cq47pqm65e5749avhzbmcbgdb3wz8czhaxazez7gdrg6cqwpywcdzyxvfh6rcrmh', location='us-east')

chris = client.feed("user", "chris")


def send_message():
    chris.add_activity({
        "actor": "chris",
        "verb": "add",
        "object": "picture:10",
        "foreign_id": "picture:10",
        "message": "Beautiful bird!"
    })

# Add an Activity; message is a custom field - tip: you can add unlimited custom fields!


# Create a following relationship between Jack's "timeline" feed and Chris' "user" feed:
jack = client.feed("timeline", "jack")
jack.follow('user', "chris")

# Read Jack's timeline and Chris' post appears in the feed:
activities = jack.get(limit=10)["results"]

# Remove an Activity by referencing it's foreign_id
chris.remove_activity(foreign_id="picture:10")