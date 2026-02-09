# Python-Grand-Strategy

Bu depo, "grand strategy" tarzında bir prototip için temel iskelet sağlar. Örnek veri ve basit bir CLI ile başlamak için hazırlanmıştır.

## Yapı

- `grand_strategy/`: Çekirdek oyun veri yapıları ve yükleyiciler.
- `data/provinces.json`: Örnek eyalet (province) verileri.

## Hızlı Başlangıç

```bash
python -m grand_strategy.cli
python -m grand_strategy.cli --province "Kuzey Yel"
```

## Notlar

- Görsel varlıklar (örn. `provinces.png`, `sea.png`, `city.png`) depoya eklenmez; kendi setinizi sağlamanız gerekir.
- Gerçek bir görsel seti veya harita çıktısı için dış kaynaklı varlıklara ihtiyaç vardır.
