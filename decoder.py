def decode_data(data, protocol):
    if protocol == "binary":
        text = "".join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
        return {"text": text}
    elif protocol == "hex":
        text = bytes.fromhex(data).decode('utf-8')
        return {"text": text}
    else:
        raise ValueError("Неизвестный протокол")
