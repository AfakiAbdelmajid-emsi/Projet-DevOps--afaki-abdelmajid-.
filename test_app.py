from app import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Bonjour" in captured.out
