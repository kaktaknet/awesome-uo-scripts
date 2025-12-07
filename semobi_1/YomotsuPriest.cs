using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Glowing Yomotsu corpse" )]
	public class YomotsuPriest : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public YomotsuPriest() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Yomotsu Priest";
			Body = 253;
			BaseSoundID = 422;

			SetStr( 480, 530 );
			SetDex( 100, 115 );
			SetInt( 600, 675 );

			SetHits( 480, 530 );
			SetMana( 600, 675 );
			SetStam( 100, 115 );

			SetDamage( 60, 80 );

			SetDamageType( ResistanceType.Physical, 100 ); 


			SetResistance( ResistanceType.Physical, 65, 85 );
			SetResistance( ResistanceType.Fire, 30, 50 );
			SetResistance( ResistanceType.Cold, 45, 65 );
			SetResistance( ResistanceType.Poison, 35, 55 );
			SetResistance( ResistanceType.Energy, 25, 50 );

			SetSkill( SkillName.MagicResist, 112.0, 122.0 );
			SetSkill( SkillName.Tactics, 55.0, 60.0 );
			SetSkill( SkillName.Wrestling, 48.0, 58.0 );
			SetSkill( SkillName.Magery, 105.0, 115.0 );
			SetSkill( SkillName.Meditation, 95.0, 110.0 );
			SetSkill( SkillName.EvalInt, 93.0, 108.0 );

			Fame = 15000;
			Karma = -15000;
			
			Tamable = false;

			
         PackGold( 700, 1000 ); 
         PackMagicItems( 1, 5 );
			AddItem( new Sandals());
			AddItem( new ExecutionersAxe());
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.Rich );
			AddLoot( LootPack.Average );
			AddLoot( LootPack.Meager );
		}

		public override bool CanRummageCorpses{ get{ return true; } }
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public YomotsuPriest( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}