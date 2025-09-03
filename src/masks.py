from typing import Union
import pytest


def get_mask_card_number(card_number: Union[str, int]) -> str:
    s = str(card_number)
    if len(s) <= 10:
        # Просто возвращаем строку, разбивая по 4 символа
        return " ".join(s[i:i+4] for i in range(0, len(s), 4))
    masked = s[:6] + "*" * (len(s) - 10) + s[-4:]
    return " ".join(masked[i:i+4] for i in range(0, len(masked), 4))


def get_mask_account(last_card_number: Union[str, int]) -> str:
    s = str(last_card_number)
    if not s:
        return "** "
    return f"** {s[-4:]}"
