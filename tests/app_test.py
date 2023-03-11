from main import formation

def test_formation():
    assert formation('Hello, {}', 'Vasya') == 'Hello, Vasya'
    assert formation('Franz {}', 'Kafka') == 'Franz Kafka'
    assert formation('Sokrat is teacher of {}', 'Platon') == 'Sokrat is teacher of Platon'