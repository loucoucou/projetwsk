def main(args):
    number = args.get("number", 0)
    doubled = args.get("doubled", 0)
    
    html_content = f"<html><body><h1>Résultats</h1><p>Le nombre original est {number} et le nombre doublé est {doubled}.</p></body></html>"
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html_content
    }
    
    return response

